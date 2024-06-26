# Generated by Django 4.2.11 on 2024-03-18 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_postimages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postimages",
            name="image",
            field=models.ImageField(upload_to="posts"),
        ),
        migrations.AlterField(
            model_name="postimages",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="blog.post",
            ),
        ),
    ]
