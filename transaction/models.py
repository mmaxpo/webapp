from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Count, Sum, Q
from django.db.models.functions.comparison import Coalesce

User = get_user_model()


class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    TRANSFER = 3
    TRANSACTION_TYPES = (
        (CHARGE, 'Charge')
        , (PURCHASE, 'Purchase')
        , (TRANSFER, 'Transfer')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPES, default=CHARGE)
    amount = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.get_transaction_type_display()} - {self.amount}'

    @classmethod
    def show_report(cls):
        positive_transactions = Sum('transactions__amount', filter=(Q(transactions__transaction_type=1)))
        negative_transactions = Sum('transactions__amount', filter=(Q(transactions__transaction_type__in=[2, 3])))
        user_balance = User.objects.all().aggregate(
            transaction_count=Count('transactions__id'),
            balance=Coalesce(positive_transactions, 0) - Coalesce(negative_transactions, 0),
        )
        return user_balance['balance']


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balance_records')
    balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.balance} - {self.created_at}'

    @classmethod
    def get_report(cls, user):
        positive_transactions = Sum('amount', filter=(Q(transaction_type=1)))
        negative_transactions = Sum('amount', filter=(Q(transaction_type__in=[2, 3])))
        user_balance = user.transactions.all().aggregate(
            balance=Coalesce(positive_transactions, 0) - Coalesce(negative_transactions, 0),
        )
        instance = cls.objects.create(user=user, balance=user_balance.get('balance', 0))
        return instance

    @classmethod
    def record_user(cls):
        for user in User.objects.all():
            record = cls.get_report(user)
            print(record)
