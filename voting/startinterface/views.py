# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.
from .models import * 
import datetime
from django.urls import reverse
from django.db.models import F

def SelectStatus(request):
    
    
    
    #modelvoice = ModelVoice.objects.filter(dateFinal__gte=timezone.now()).filter(status=True)
    for i in ModelVoice.objects.filter(dateFinal__lt=timezone.now()).filter(status=True):
        i.status=False
        i.save()    
    modelvoice = ModelVoice.objects.filter(status=True)

    return render(request, "startinterface/apphtml.html", {'modelvoice': modelvoice})

def CompletedVoiting(request):
    modelvoice = ModelVoice.objects.filter(status=False)
    return render(request, "startinterface/ListCompleted.html", {'modelvoice': modelvoice})

def DetaleActive(request):
    
    modelvoice = ModelVoice.objects.get(pk = request.GET['id'])

    if modelvoice.status==False:
        return HttpResponse('End')
    else: return render(request, "startinterface/DetaleActive.html", {'modelvoice': modelvoice.person.all(), 'nameVoice':modelvoice.nameVoice}) 
    #return HttpResponse(modelvoice.person.all())

def DetaleCompleted(request):
    print 'buga'
    
    personevoice = ModelPersonVoice.objects.filter(nameVoice = ModelVoice.objects.get(pk = request.GET['id']).nameVoice).order_by('-changeVoice')

    
    return render(request, "startinterface/DetaleCompleted.html", {'personevoice':personevoice}) 
 

def Handler(request):
    
    modelvoice = ModelPersonVoice.objects.filter(person = request.POST['person'])
    if modelvoice.exists():
        print request.POST['person']
        print request.POST['nameVoice']
        modelvoice2 = ModelPersonVoice.objects.filter(person = request.POST['person']).filter(nameVoice = request.POST['nameVoice'])
        
        if modelvoice2.exists():
            print modelvoice2.update(changeVoice=F('changeVoice')+1)
            #modelvoice2[0].changeVoice+=1
            #print modelvoice2[0].changeVoice
            #modelvoice2[0].save()

            if modelvoice2[0].changeVoice >= ModelVoice.objects.filter(nameVoice = request.POST['nameVoice'])[0].maxVoice:
                b = ModelVoice.objects.get(nameVoice = request.POST['nameVoice'])
                b.status = False
                b.save()
                
        else:
            a = ModelPersonVoice(person = request.POST['person'], nameVoice = request.POST['nameVoice'], changeVoice=1)	
            a.save()
    else:
        a = ModelPersonVoice(person = request.POST['person'], nameVoice = request.POST['nameVoice'], changeVoice=1)
        a.save()    
    #return HttpResponse('Thank you!')
    return HttpResponseRedirect(reverse('SelectStatus'))
    #return HttpResponse(modelvoice.person.all())
        