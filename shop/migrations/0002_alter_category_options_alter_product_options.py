# Generated by Django 4.1.7 on 2023-03-26 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("name",),
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name",),
                "verbose_name": "product",
                "verbose_name_plural": "products",
            },
        ),
    ]
