# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-22 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import portal.models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20170921_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to=portal.models.get_file_name),
        ),
    ]
