from django.contrib import admin
from basket.models import *


class BasketInline(admin.TabularInline):
    model = BasketItem
    extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    inlines = [BasketInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'basket', 'product', 'quantity']
