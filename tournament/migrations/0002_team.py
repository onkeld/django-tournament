# Generated by Django 5.0.4 on 2024-04-28 10:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=255, verbose_name='Team Name')),
                ('club', models.CharField(max_length=255, verbose_name='Club Name')),
                ('city', models.CharField(max_length=75, verbose_name='City of Origin')),
                ('country', models.CharField(default='Germany', max_length=255, verbose_name='Country of Origin')),
                ('primary_colour', models.CharField(max_length=50, verbose_name='Main Team Colour Scheme')),
                ('secondary_colour', models.CharField(max_length=50, verbose_name='Secondary Team Colour Scheme')),
                ('team_manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Team Manager')),
            ],
        ),
    ]