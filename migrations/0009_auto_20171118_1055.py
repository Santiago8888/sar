# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sar', '0008_auto_20171117_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jahre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.FloatField(blank=True, default=0, null=True)),
                ('Total', models.FloatField(blank=True, default=0, null=True)),
                ('Anyo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anyo_jahre', to='sar.Anyo', verbose_name='anyo_jahre')),
            ],
        ),
        migrations.CreateModel(
            name='Monat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.FloatField(blank=True, default=0, null=True)),
                ('Total', models.FloatField(blank=True, default=0, null=True)),
                ('Mes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_monat', to='sar.Mes', verbose_name='mes_monat')),
            ],
        ),
        migrations.CreateModel(
            name='Woche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.FloatField(blank=True, default=0, null=True)),
                ('Total', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='semana',
            name='Fin',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='semana',
            name='Inicio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='woche',
            name='Semana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semana_woche', to='sar.Semana', verbose_name='semana_woche'),
        ),
    ]
