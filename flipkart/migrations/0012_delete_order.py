# Generated by Django 4.2.4 on 2023-09-11 14:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("flipkart", "0011_rename_product_name_product_product_name"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Order",
        ),
    ]
