# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-23 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20170922_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='blur',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], default='n', max_length=5),
        ),
        migrations.AddField(
            model_name='document',
            name='flip',
            field=models.CharField(choices=[('horizon', 'Flip Horizontally'), ('vertical', 'Flip Vertically'), ('NONE', 'None')], default='NONE', max_length=17),
        ),
        migrations.AddField(
            model_name='document',
            name='rotate',
            field=models.CharField(choices=[('clock', 'Clockwise'), ('anti', 'Anticlockwise'), ('NONE', 'None')], default='NONE', max_length=15),
        ),
        migrations.AddField(
            model_name='document',
            name='size',
            field=models.IntegerField(choices=[(1, 'Large'), (2, 'Medium'), (3, 'Small')], default=1),
        ),
    ]
