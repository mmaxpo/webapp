# Generated by Django 4.2.11 on 2024-04-02 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shipping", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shippingaddress",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]