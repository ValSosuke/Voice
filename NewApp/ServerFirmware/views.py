# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

import os
from jinja2 import Environment
from django.http import HttpResponse
def index(request):
    return render(request, "ServerFirmware/apphtml.html")
def contact(request):
    return render(request, "ServerFirmware/ppp.html",{'value':["Пизда", "Сиська"],})
# Create your views here.
