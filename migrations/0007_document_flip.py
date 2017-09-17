# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_remove_document_flip'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='flip',
            field=models.CharField(choices=[('horizon', 'Flip Horizontally'), ('vertical', 'Flip Vertically'), ('NONE', 'None')], default='NONE', max_length=17),
        ),
    ]
