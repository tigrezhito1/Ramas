# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-27 23:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colasIN', '0011_auto_20181227_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 27, 23, 41, 9, 859984)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2018, 12, 27, 23, 41, 9, 865585)),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 27, 23, 41, 9, 866126), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 27, 23, 41, 9, 865000)),
        ),
    ]
