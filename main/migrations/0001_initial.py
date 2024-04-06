# Generated by Django 3.2.25 on 2024-04-06 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.TextField()),
                ('user_role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='The_Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='admin', serialize=False, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='The_Client',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='client', serialize=False, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='The_Trainer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='trainer', serialize=False, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.the_client')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.the_trainer')),
            ],
        ),
    ]
