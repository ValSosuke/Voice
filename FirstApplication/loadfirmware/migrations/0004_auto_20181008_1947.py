# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-08 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loadfirmware', '0003_auto_20181007_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablebinaryfw',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='tablebinaryfw',
            name='valn_function_name',
        ),
    ]