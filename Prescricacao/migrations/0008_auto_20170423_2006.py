# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 23:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prescricacao', '0007_auto_20170423_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leito',
            old_name='codigodoleito',
            new_name='codigoleito',
        ),
    ]
