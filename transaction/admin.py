from django.contrib import admin

from transaction.models import UserBalance, Transaction


@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'created_at']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_type', 'amount', 'created_at']
