# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 15:58
from __future__ import unicode_literals
from datetime import datetime

from django.db import migrations, models


def set_approved(apps, schema_editor):  # pylint: disable=unused-argument
    Fund = apps.get_model("lowfat", "Fund")  # pylint: disable=invalid-name
    for fund in Fund.objects.all():
        if fund.status == "A":
            fund.approved = datetime.now()
            fund.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0102_auto_20170510_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='approved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.RunPython(set_approved),
        migrations.AddField(
            model_name='historicalfund',
            name='approved',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
