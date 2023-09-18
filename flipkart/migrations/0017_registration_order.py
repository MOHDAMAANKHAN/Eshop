# Generated by Django 4.2.4 on 2023-09-11 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("flipkart", "0016_delete_order_delete_registration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.CharField(blank=True, max_length=50, null=True)),
                ("password", models.CharField(blank=True, max_length=255, null=True)),
                ("mobile", models.BigIntegerField(default=0)),
                ("gender", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("mobile", models.BigIntegerField()),
                ("price", models.BigIntegerField()),
                ("quantity", models.IntegerField()),
                ("status", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flipkart.registration",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flipkart.product",
                    ),
                ),
            ],
        ),
    ]
