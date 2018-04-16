# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    dependencies = [
        ('lowfat', '0128_auto_20180413_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=True, help_text='Will not be deleted when the count reaches 0')),
                ('path', models.TextField()),
                ('label', models.CharField(help_text='The name of the tag, without ancestors', max_length=255)),
                ('level', models.IntegerField(default=1, help_text='The level of the tag in the tree')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='lowfat.FundActivity')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagTreeModel, models.Model),
        ),
        migrations.AddField(
            model_name='fund',
            name='activity',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, autocomplete_view=None, force_lowercase=True, help_text='Enter a comma-separated tag string', initial='attending as ssi, conference, field trip, focus group, hack, knowledge exchange, local, meeting, new paradigm, new resource, organising submeeting, panel, paying for others, policy, poster presentation, prize, roundtable, roundtable/lead, software Special Interest Group, ssi organised, supported collaborator, survey, talk at, talk at/invited, teaching at, teaching as helper, training/attending, training/organiser, unconference, working group, workshop', to='lowfat.FundActivity', tree=True),
        ),
        migrations.AlterUniqueTogether(
            name='fundactivity',
            unique_together=set([('slug', 'parent')]),
        ),
    ]