# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-07 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadfirmware', '0002_tablebinaryfw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablebinaryfw',
            name='data_binary',
            field=models.BinaryField(),
        ),
    ]