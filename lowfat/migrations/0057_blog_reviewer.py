# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 09:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lowfat', '0056_auto_20160808_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
