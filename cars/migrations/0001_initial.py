# Generated by Django 5.1 on 2024-09-07 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Cars",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("model", models.CharField(max_length=200)),
                ("factory_year", models.IntegerField(blank=True, null=True)),
                ("model_year", models.IntegerField(blank=True, null=True)),
                ("plate", models.CharField(blank=True, max_length=10, null=True)),
                ("value", models.FloatField(blank=True, null=True)),
                ("photo", models.ImageField(blank=True, null=True, upload_to="cars/")),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="car_brand",
                        to="cars.brand",
                    ),
                ),
            ],
        ),
    ]
