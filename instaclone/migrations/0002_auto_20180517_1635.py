# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-17 13:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_prof',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
