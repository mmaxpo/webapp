# Generated by Django 4.2.11 on 2024-03-20 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("basket", "0002_rename_quantity_product_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basketitem",
            name="basket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items_basket",
                to="basket.basket",
            ),
        ),
        migrations.AlterField(
            model_name="basketitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items_product",
                to="basket.product",
            ),
        ),
    ]
