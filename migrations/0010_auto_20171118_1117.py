# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sar', '0009_auto_20171118_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='semana',
            name='FMes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='semana',
            name='IMes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
