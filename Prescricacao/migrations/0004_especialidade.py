# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prescricacao', '0003_auto_20170419_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=1)),
            ],
        ),
    ]