# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 09:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaclone', '0002_auto_20180517_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='uploaded_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user_prof',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user_prof',
            name='mail_confirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user_prof',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]