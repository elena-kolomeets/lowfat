# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0123_auto_20180206_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='termsandconditions',
            options={'ordering': ['-year']},
        ),
    ]