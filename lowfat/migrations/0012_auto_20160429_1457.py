# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0011_auto_20160429_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fellow',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lowfat.Fellow'),
        ),
    ]
