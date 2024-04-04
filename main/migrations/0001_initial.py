# Generated by Django 5.0.4 on 2024-04-04 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=50)),
                ("user_role", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="The_Admin",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="admin",
                        serialize=False,
                        to="main.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="The_Client",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="client",
                        serialize=False,
                        to="main.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="The_Trainer",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="trainer",
                        serialize=False,
                        to="main.user",
                    ),
                ),
            ],
        ),
    ]
