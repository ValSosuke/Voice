# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.
from .models import * 
import datetime
from django.urls import reverse
from django.db.models import F
from django.forms import ModelForm
from .models import ModelPerson
from django.http import Http404
from django.contrib import auth

class ArticleForm(ModelForm):
    class Meta:
        model = ModelPerson
        fields = "__all__" 

def SelectStatus(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('accounts/login/')
    modelvoice=[]
    listobjaects = ModelVoice.objects.all()
    if listobjaects:
        for e in listobjaects:
            if e.status == True:
                modelvoice.append(e)
    
    return render(request, "startinterface/apphtml.html", {'modelvoice': modelvoice, 'req' : request})
    
def CompletedVoiting(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('accounts/login/')
    modelvoice=[]
    listobjaects = ModelVoice.objects.all()
    
    if listobjaects:
        for e in listobjaects:
            if e.status == False:
                modelvoice.append(e)
    return render(request, "startinterface/ListCompleted.html", {'modelvoice': modelvoice})

def DetaleActive(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('accounts/login/')
    modelvoice = get_object_or_404(ModelVoice, pk = request.GET['id'])
    return render(request, "startinterface/DetaleActive.html", {'modelvoice': modelvoice}) 
    
def DetaleCompleted(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('accounts/login/')
    personevoice = ModelPersonVoice.objects.filter(voice__id_name = request.GET['id']).order_by('-changeVoice')
    if personevoice:
        return render(request, "startinterface/DetaleCompleted.html", {'personevoice':personevoice}) 
    else: raise Http404()

def Handler(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('accounts/login/')    
    #voice1 = ModelPersonVoice.objects.get(voice__id_name = request.POST['voice'], person__id_name = request.POST['person'] )
    voice1 = get_object_or_404(ModelPersonVoice, voice__id_name = request.POST['voice'], person__id_name = request.POST['person'])
    voice1.changeVoice+=1
    voice1.save()
    return HttpResponseRedirect(reverse('SelectStatus'))
    
def logined(request):
    if request.method == 'POST':
        login = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=login, password=password)
        if user is not None:
            HttpResponseRedirect(reverse('SelectStatus'))
        else:
            HttpResponseRedirect(reverse('aauth'))
    else:
        raise Http404()