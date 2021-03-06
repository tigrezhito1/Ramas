# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-17 12:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colasIN', '0034_auto_20190117_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 97298)),
        ),
        migrations.AlterField(
            model_name='agente',
            name='t_estado',
            field=models.DateTimeField(db_column='t_estado', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 97475)),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 125175)),
        ),
        migrations.AlterField(
            model_name='logestadoagente',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 94563)),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 12, 1, 51, 127169), editable=False, help_text='Fecha de recepci\xf3n de la llamada (No se puede modificar)'),
        ),
        migrations.AlterField(
            model_name='produccionaudio',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2019, 1, 17, 12, 1, 51, 136444)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 12, 1, 51, 122840)),
        ),
    ]
