# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulate', '0004_auto_20170417_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulatedetails',
            name='material',
        ),
        migrations.AlterField(
            model_name='formulate',
            name='category',
            field=models.IntegerField(),
        ),
    ]
