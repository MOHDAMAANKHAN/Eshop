# Generated by Django 4.2.4 on 2023-09-07 13:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("flipkart", "0005_product"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="product_category",
            new_name="Product_category",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="product_desc",
            new_name="Product_desc",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="product_price",
            new_name="Product_price",
        ),
    ]
