# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-20 23:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0082_auto_20181220_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 20, 23, 34, 13, 639830)),
        ),
        migrations.AlterField(
            model_name='api',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 20, 23, 34, 13, 637108)),
        ),
        migrations.AlterField(
            model_name='base',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 20, 23, 34, 13, 634617)),
        ),
        migrations.AlterField(
            model_name='campania',
            name='fecha',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2018, 12, 20, 23, 34, 13, 631210)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 20, 23, 34, 13, 626205)),
        ),
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 20, 23, 34, 13, 629023)),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 20, 23, 34, 13, 624209)),
        ),
    ]
