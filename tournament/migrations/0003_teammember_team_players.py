# Generated by Django 5.0.4 on 2024-04-28 12:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_team'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(verbose_name='Jersey Number')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(related_name='players', through='tournament.TeamMember', to=settings.AUTH_USER_MODEL),
        ),
    ]