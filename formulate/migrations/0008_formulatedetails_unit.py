# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulate', '0007_auto_20170417_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulatedetails',
            name='unit',
            field=models.CharField(default='公克', max_length=20),
        ),
    ]
