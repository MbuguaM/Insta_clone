# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0004_auto_20180528_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('PRIVATE', 'private'), ('PUBLIC', 'public')], default='PRIVATE', max_length=30),
        ),
    ]
