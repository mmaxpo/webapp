from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

    def active(self):
        return self.get_queryset().filter(is_active=True)


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shipping_address')
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)

    objects = MyManager()
