# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django import forms

#class NameForm(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=100)


class ModelPerson(models.Model):
    id_name = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images', null=False, blank=True)
    age = models.IntegerField()
			
class ModelVoice(models.Model):
    """docstring for TableName"""
    id_name = models.AutoField(primary_key=True)
    nameVoice = models.CharField(max_length=50)
    dateStart = models.DateTimeField()
    dateFinal = models.DateTimeField()
    maxVoice = models.IntegerField()
    person = models.ManyToManyField(ModelPerson)
    status = models.BooleanField(default=True)
    #listOfPerson = models.CharField(max_length=50)

class ModelPersonVoice(models.Model):
    id_name = models.AutoField(primary_key=True)
    person = models.CharField(max_length=50)
    nameVoice = models.CharField(max_length=50)
    changeVoice = models.IntegerField()
    
		