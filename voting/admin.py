from django.contrib import admin
from .startinterface.models import *
from .template.models import * 
admin.site.register(ModelPerson)
admin.site.register(ModelVoice)
admin.site.register(ModelPersonVoice)
