# Generated by Django 5.1 on 2024-10-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarInventory",
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
                ("cars_count", models.IntegerField()),
                ("cars_value", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddField(
            model_name="cars",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
