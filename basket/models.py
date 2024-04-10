from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def add(self, product, qty=1):
        if self.items_basket.filter(product=product).exists():
            product_items = self.items_basket.filter(product=product).first()
            product_items.quantity += int(qty)
            product_items.save()
        else:
            product_items = self.items_basket.create(product=product, quantity=qty)
        return product_items

    def __str__(self):
        return f' basket id: {self.id}'


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='items_basket')
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items_product')

    def __str__(self):
        return f'{self.basket} - {self.quantity} - {self.product}'
