# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django import forms
from datetime import datetime 
from datetime import date
from django.utils import timezone
from django.db.models import F
#class NameForm(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=100)


class ModelPerson(models.Model):
    id_name = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="gallery")
    datee = models.DateField()
    def age(self):
        today = date.today()
        return today.year - self.datee.year - ((today.month, today.day) < (self.datee.month, self.datee.day))
    def __unicode__(self):
        return self.name
class ModelVoice(models.Model):
    """docstring for TableName"""

    id_name = models.AutoField(primary_key=True)
    nameVoice = models.CharField(max_length=50)
    dateStart = models.DateTimeField()
    dateFinal = models.DateTimeField()
    maxVoice = models.IntegerField()
    person = models.ManyToManyField(ModelPerson, through = 'ModelPersonVoice')
    status = models.BooleanField()
    @property
    def status(self):
        mm = ModelPersonVoice.objects.filter(voice__id_name=self.id_name).filter(changeVoice__gte=self.maxVoice)
        if mm:
            return False    
        if timezone.now()>=self.dateFinal:
            return  False
        return True

    def __unicode__(self):
        return self.nameVoice
    #listOfPerson = models.CharField(max_length=50)

class ModelPersonVoice(models.Model):
    id_name = models.AutoField(primary_key=True)
    person = models.ForeignKey(ModelPerson, on_delete=models.CASCADE)
    voice = models.ForeignKey(ModelVoice, on_delete=models.CASCADE)
    changeVoice = models.IntegerField()
    

