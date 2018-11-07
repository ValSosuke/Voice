# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django import forms

#class NameForm(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=100)
class TableNameFW(models.Model):
    """docstring for TableName"""
    id_name = models.AutoField(primary_key=True)
    name_firmawre_1 = models.CharField(max_length=50)
    name_firmawre_2 = models.CharField(max_length=50)

class TableScriptsFW(models.Model):
    id_name = models.IntegerField()
    script_name = models.CharField(max_length=50)
    data_script = models.TextField()

class TableHtmlFW(models.Model):
    id_name = models.IntegerField()
    html_name = models.CharField(max_length=50)
    data_html = models.TextField()

class TableOtherFW(models.Model):
    id_name = models.IntegerField()
    other_name = models.CharField(max_length=50)
    data_other = models.TextField()

class TableConfigureFW(models.Model):
    id_name = models.IntegerField()
    configure_name = models.CharField(max_length=50)
    data_configure = models.TextField()

class TableBinaryFW(models.Model):
    id_name = models.IntegerField()
    valn_function_name = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    data_binary = models.TextField()