# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import * 
class PersonAdmin(admin.ModelAdmin):
    save_as = True
admin.site.register(ModelPerson, PersonAdmin)
admin.site.register(ModelVoice)
admin.site.register(ModelPersonVoice)
