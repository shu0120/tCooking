# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulate', '0010_auto_20170417_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulate',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='upload'),
        ),
    ]
