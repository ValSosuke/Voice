# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from loadfirmware.models import *
import pickle
def wives_fw(request):
    tablenamefw = TableNameFW.objects.all()

    return render(request, 'news/posts.html', {'tablenamefw': tablenamefw})

def wives_post(request):
    message = request.GET.get('id_name')
    print message

    tablenamefw = TableNameFW.objects.all()
    tablescriptfw = TableScriptsFW.objects.all()
    tablehtmlfw = TableHtmlFW.objects.all()
    tableotherfw = TableOtherFW.objects.all()
    tableconfigurefw = TableConfigureFW.objects.all()
    tablebinaryfw = TableBinaryFW.objects.all()
    list_script = []
    list_html = []

    list_configure = []
    list_other = []
    list_all_binary = []
    for i in tablescriptfw:
        if str(i.id_name) == message:
            list_script.append([i.script_name, i.data_script])

    for i in tablehtmlfw:
        if str(i.id_name) == message:
            list_html.append([i.html_name, i.data_html])

    for i in tableotherfw:
        if str(i.id_name) == message:
            list_other.append([i.other_name, i.data_other])

    for i in tableconfigurefw:
        if str(i.id_name) == message:
            list_configure.append([i.configure_name, i.data_configure])
                        
    for i in tablebinaryfw:
        if str(i.id_name) == message:
            #if len(list_all_binary)==0:
            list_all_binary = pickle.loads(i.data_binary)
            break
            #else:
            #    cc=0	
#
 #               for j in list_all_binary:
  #              	
   #                 if i.valn_function_name==j[0]:
    #                    cc=1	
     #                   j[1].append([i.file_name, i.data_binary])
      #                  break
       #         if cc==0:
        #            list_all_binary.append([i.valn_	function_name,[i.file_name, i.data_binary]])       

    return render(request, 'loadfirmware/viwer.html', {'list_script': list_script, 'list_html':list_html, 'list_configure':list_configure, 'list_other':list_other, 'list_all_binary':list_all_binary})
# Create your views here.
