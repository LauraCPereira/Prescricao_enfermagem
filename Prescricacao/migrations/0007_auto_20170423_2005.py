# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prescricacao', '0006_auto_20170423_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leito',
            old_name='nome',
            new_name='codigodoleito',
        ),
        migrations.RemoveField(
            model_name='prescricaodeenfermagem',
            name='turno',
        ),
        migrations.AddField(
            model_name='prescricaodeenfermagem',
            name='descricao',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescricaodeenfermagem',
            name='diagnostico',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescricaodeenfermagem',
            name='horario',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
