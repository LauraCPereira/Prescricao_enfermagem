# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 22:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prescricacao', '0002_auto_20170418_0948'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Leito',
        ),
        migrations.AddField(
            model_name='prescricaodeenfermagem',
            name='numleito',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescricaodeenfermagem',
            name='turno',
            field=models.IntegerField(choices=[(1, 'Manhã'), (2, 'Tarde'), (3, 'Noite')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='prescricaodeenfermagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prescricacao.PrescricaoDeEnfermagem'),
        ),
    ]
