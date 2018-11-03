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
from django.forms import ModelForm
from .models import ModelPerson

class ArticleForm(ModelForm):
    class Meta:
        model = ModelPerson
        fields = "__all__" 
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
    formm = ArticleForm()
    modelss = ModelPerson()
    if modelvoice.status==False:
        return HttpResponse('End')

    else: return render(request, "startinterface/DetaleActive.html", {'modelss':modelss,'modelvoice': modelvoice}) 
    #return HttpResponse(modelvoice.person.all())

def DetaleCompleted(request):
    
    
    personevoice = ModelPersonVoice.objects.filter(voice__id_name = request.GET['id']).order_by('-changeVoice')

    
    return render(request, "startinterface/DetaleCompleted.html", {'personevoice':personevoice}) 
 

def Handler(request):
    
    #modelvoice = ModelPersonVoice.objects.filter(id = request.POST['person'])
    #if modelvoice.exists():
    #    modelvoice2 = ModelPersonVoice.objects.filter(id = request.POST['person']).filter(nameVoice = request.POST['nameVoice'])
    #    request.POST['person']
    #    if modelvoice2.exists():
    #        print modelvoice2.update(changeVoice=F('changeVoice')+1)
            #modelvoice2[0].changeVoice+=1
            #print modelvoice2[0].changeVoice
            #modelvoice2[0].save()

    #        if modelvoice2[0].changeVoice >= ModelVoice.objects.filter(nameVoice = request.POST['nameVoice'])[0].maxVoice:
    #            b = ModelVoice.objects.get(nameVoice = request.POST['nameVoice'])
    #            b.status = False
    #            b.save()
                
    #    else:
    #        a = ModelPersonVoice(person = request.POST['person'], nameVoice = request.POST['nameVoice'], changeVoice=1)	
    #        a.save()
    #else:
    #    a = ModelPersonVoice(person = request.POST['person'], nameVoice = request.POST['nameVoice'], changeVoice=1)
     #   a.save()    
    #return HttpResponse('Thank you!')
    #people_in_group = ModelPerson.objects.filter(modelpersonvoice_set__voice = request.POST['voice'])
    
    voice1 = ModelPersonVoice.objects.get(voice__id_name = request.POST['voice'], person__id_name = request.POST['person'] )
    
    voice1.changeVoice+=1
    
    if (voice1.changeVoice>=ModelVoice.objects.get(id_name=request.POST['voice']).maxVoice):
        b = ModelVoice.objects.get(id_name=request.POST['voice'])
        b.status = False
        b.save()
    #b = ModelPersonVoice.objects.filter(voice = ModelVoice.objects.get(nameVoice = request.POST['voice']))    
    voice1.save()
    return HttpResponseRedirect(reverse('SelectStatus'))
    #return HttpResponse(modelvoice.person.all())
        