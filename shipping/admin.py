from django.contrib import admin

from shipping.models import ShippingAddress


@admin.register(ShippingAddress)
class ShiipingAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'address', 'is_active']
