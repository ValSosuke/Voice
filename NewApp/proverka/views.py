# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from loadfirmware.models import *
import pickle
def wives_fw(request):
    tablenamefw = TableNameFW.objects.all()

    return render(request, 'news/posts.html')


