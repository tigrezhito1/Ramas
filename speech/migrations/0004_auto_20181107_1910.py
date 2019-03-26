# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-07 19:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0003_auto_20181107_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 10, 35, 479465)),
        ),
        migrations.AlterField(
            model_name='api',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 10, 35, 477648)),
        ),
        migrations.AlterField(
            model_name='base',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 10, 35, 476158)),
        ),
        migrations.AlterField(
            model_name='campania',
            name='fecha',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2018, 11, 7, 19, 10, 35, 473939)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 10, 35, 471926)),
        ),
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 10, 35, 473285)),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 11, 7, 19, 10, 35, 470931)),
        ),
        migrations.AlterModelTable(
            name='dblaster',
            table='speech_d_blaster',
        ),
        migrations.AlterModelTable(
            name='dllamadas',
            table='speech_d_llamadas',
        ),
    ]
