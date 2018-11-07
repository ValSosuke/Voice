# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import os
import shutil
import glob
import random
import mmap
import sys
from contextlib import closing
import struct
import binascii
import commands    
import magic
import requests
from signal import signal, SIGPIPE, SIG_DFL
import binascii, subprocess
import re
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
#import pdb; pdb.set_trace()
file=None
#from somewhere import handle_uploaded_file
class header_sqashfs4:

    s_magic=b""
    inodes=0
    mkfs_time=0
    block_size=0
    fragments=0
    compression=0
    block_log=0
    flags=0
    no_ids=0
    s_major=0
    s_minor=0
    root_inode=0
    bytes_used=0
    id_table_start=0
    xattr_id_table_start=0
    inode_table_start=0
    directory_table_start=0
    fragment_table_start=0
    lookup_table_start=0
		
class header_sqashfs3:

    s_magic=b""
    inodes=0
    bytes_used_2=0
    uid_start_2=0
    guid_start_2=0
    inode_table_start_2=0
    directory_table_start_2=0
    s_major=0
    s_minor=0
    block_size_1=0
    block_log=0
    flags=0
    no_uids=0
    no_guids=0
    mkfs_time=0
    root_inode=0
    block_size=0
    fragments=0
    fragment_table_start_2=0
    bytes_used=0
    uid_start=0
    guid_start=0
    inode_table_start=0
    directory_table_start=0
    fragment_table_start=0
    lookup_table_start=0

def read_struct(n,big_or_little):
    global file
    
    a=file.read(n)
    
    if (binascii.hexlify(a)=="".join(["ff" for z in range(n)])):
        return -1
    else:
    	if (n==1):
            return struct.unpack(big_or_little+'B', a)[0]
        elif (n==2):
            return struct.unpack(big_or_little+'H', a)[0]
        elif (n==4):
            return struct.unpack(big_or_little+'L', a)[0]
        elif (n==8):
            return struct.unpack(big_or_little+'Q', a)[0]

def end_of_sqashfs(file,start,big_or_little):
    
    fragments_per_index_block=512
    index_entry_size_bytes= 8
    
    file.seek(start+28)
    aaa = file.read(2)
    
    
    
    major_version=struct.unpack(big_or_little+'H', aaa)[0]	
    
    #print binascii.hexlify(aaa)
    
    if (major_version == 3):
        obj_struct=header_sqashfs3()
        header = 119
        file.seek(start)
        obj_struct.s_magic=file.read(4)
        obj_struct.inodes=read_struct(4,big_or_little)
        obj_struct.bytes_used_2=read_struct(4,big_or_little)
        obj_struct.uid_start_2=read_struct(4,big_or_little)
        obj_struct.guid_start_2=read_struct(4,big_or_little)
        obj_struct.inode_table_start_2=read_struct(4,big_or_little)
        obj_struct.directory_table_start_2=read_struct(4,big_or_little)
        obj_struct.s_major=read_struct(2,big_or_little)
        obj_struct.s_minor=read_struct(2,big_or_little)
        obj_struct.block_size_1=read_struct(2,big_or_little)
        obj_struct.block_log=read_struct(2,big_or_little)
        obj_struct.flags=read_struct(1,big_or_little)
        obj_struct.no_uids=read_struct(1,big_or_little)
        obj_struct.no_guids=read_struct(1,big_or_little)
        obj_struct.mkfs_time=read_struct(4,big_or_little)
        obj_struct.root_inode=read_struct(8,big_or_little)
        obj_struct.block_size=read_struct(4,big_or_little)
        obj_struct.fragments=read_struct(4,big_or_little)
        obj_struct.fragment_table_start_2=read_struct(4,big_or_little)
        obj_struct.bytes_used=read_struct(8,big_or_little)
        obj_struct.uid_start=read_struct(8,big_or_little)
        obj_struct.guid_start=read_struct(8,big_or_little)
        obj_struct.inode_table_start=read_struct(8,big_or_little)
        obj_struct.directory_table_start=read_struct(8,big_or_little)
        obj_struct.fragment_table_start=read_struct(8,big_or_little)
        obj_struct.lookup_table_start=read_struct(8,big_or_little)

    elif(major_version == 4):
        obj_struct=header_sqashfs4()
        header = 96

        file.seek(start)
        obj_struct.s_magic=file.read(4)
        obj_struct.inodes=read_struct(4,big_or_little)
        obj_struct.mkfs_time=read_struct(4,big_or_little)
        obj_struct.block_size=read_struct(4,big_or_little)
        obj_struct.fragments=read_struct(4,big_or_little)
        obj_struct.compression=read_struct(2,big_or_little)
        obj_struct.block_log=read_struct(2,big_or_little)
        obj_struct.flags=read_struct(2,big_or_little)
        obj_struct.no_ids=read_struct(2,big_or_little)
        obj_struct.s_major=read_struct(2,big_or_little)
        obj_struct.s_minor=read_struct(2,big_or_little)
        obj_struct.root_inode=read_struct(8,big_or_little)
        obj_struct.bytes_used=read_struct(8,big_or_little)
        obj_struct.id_table_start=read_struct(8,big_or_little)
        obj_struct.xattr_id_table_start=read_struct(8,big_or_little)
        obj_struct.inode_table_start=read_struct(8,big_or_little)
        obj_struct.directory_table_start=read_struct(8,big_or_little)
        obj_struct.fragment_table_start=read_struct(8,big_or_little)
        obj_struct.lookup_table_start=read_struct(8,big_or_little)

    else:
        return -1
    
    



    #if (major_version == 3):
    
     #   if (sqsb.no_uids > 0)
     
      #      uint32 uid_table[sqsb.no_uids];
    
    
       # if (sqsb.no_guids > 0)
    
    #        uint32 gid_table[sqsb.no_guids];
     



    
    file_data=obj_struct.inode_table_start - header
    inode_table= obj_struct.directory_table_start - obj_struct.inode_table_start
    file.seek(start+obj_struct.fragment_table_start)
    directory_table=(struct.unpack(big_or_little+'Q', file.read(8))[0]-obj_struct.directory_table_start)
    file.seek(start+obj_struct.fragment_table_start)
    fragment_table=(obj_struct.fragment_table_start-struct.unpack(big_or_little+'Q', file.read(8))[0])
    fragment_table_index= 1+(obj_struct.fragments/fragments_per_index_block)
    
    #export_table
    
    
    #id_table
    if (major_version == 3):
        id_table_start = obj_struct.uid_start
    elif (major_version == 4):
        file.seek( start+obj_struct.id_table_start)
        id_table_start = struct.unpack(big_or_little+'Q', file.read(8))[0]
    else:
        
        return -1
    
    if (obj_struct.lookup_table_start != -1):
       
        export_table=id_table_start - obj_struct.fragment_table_start - fragment_table_index*index_entry_size_bytes
    else:
    	export_table=0

    if (major_version == 3):
    	if (obj_struct.no_uids>0):
    		uid_table = obj_struct.no_uids
    	if (obj_struct.no_guids>0):
    		gid_table = obj_struct.no_guids
    elif (major_version == 4):
        if (obj_struct.xattr_id_table_start != -1):
            id_table_size = obj_struct.xattr_id_table_start - id_table_start    
        else:
            id_table_size = obj_struct.bytes_used - id_table_start
        id_table = id_table_size;	
    else:
        return -1
    
    
        
    
    

    padding= 4096 - (obj_struct.bytes_used % 4096)
    
    if (major_version == 4):
        end=int(sum([header,file_data,inode_table,directory_table,fragment_table,fragment_table_index*8,export_table,id_table,padding]))
    elif (major_version == 3):
        end=int(sum([header,file_data,inode_table,directory_table,fragment_table,fragment_table_index*8,export_table,uid_table*4,padding]))
        #print obj_struct.s_magic
        #print obj_struct.inodes
        #print obj_struct.bytes_used_2
        #print obj_struct.uid_start_2
        #print obj_struct.guid_start_2
        #print obj_struct.inode_table_start_2
        #print obj_struct.directory_table_start_2
        #print obj_struct.inode_table_start
        #print header
        #print file_data
        #print inode_table
        #print directory_table
        #print fragment_table
        #print fragment_table_index
        #print export_table
        #print uid_table
        #print padding
        print obj_struct.inodes
    else: 
        return -1
    #print end

    return end, obj_struct
filess = {}

def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf
    
def handle_uploaded_file(patth_dir,f,f1,n):

    global file, filess
    m=magic.open(magic.MAGIC_NONE)
    m.load() 
    #files = glob.glob('/tmp/Django_files/*')
    i=0
    pattern=[["sqsh",">"],["sqlz",">"],["qshs",">"],["tqsh",">"],["hsqs","<"],["hsqt","<"],["shqs","<"]]

    for fs in f:
    
        with open(patth_dir+fs.name, 'wb+') as destination:
            for chunk in fs.chunks():
                destination.write(chunk)
#                filess.update("uploades"+i:patth_dir+fs.name)
        i+=1
        destination.close()
    i=0
    for fs in f1:
    
        with open(patth_dir+fs.name, 'wb+') as destination:
            for chunk in fs.chunks():
                destination.write(chunk)
#                filess.update("uploades"+i:patth_dir+fs.name)
        i+=1
        destination.close()
        
    i=0
    for fs in f:
        with open(patth_dir+fs.name, 'rb+',0) as destination1, closing(mmap.mmap(destination1.fileno(), 0, access=mmap.ACCESS_READ)) as s:
            file=destination1
            buff=destination1.read()
            big_little=""
            for ij in pattern:
                
                start=s.find(ij[0])
                if start>=0:
                    big_little=ij[1]
                    break            
            struct_firmware=None
            end, struct_firmware=end_of_sqashfs(destination1,start,big_little)
            catch_buff=buff[start:(start+end)]
            if (fs.name.find("(")>=0):
                fs.name = fs.name[0:fs.name.find("(")]
            catch_squashfs_file=open(patth_dir+fs.name+'.squash', 'wb+')
            catch_squashfs_file.write(catch_buff)
            catch_squashfs_file.close()
            st=""
            if (struct_firmware.s_major==4):
                if (struct_firmware.compression==2):
                    #st="./Squashfs/squashfs-all/unsquashfs/unsquashfs_lzma_4.0 " + "-f -d "+ patth_dir+"/FS" + str(i) +" " +patth_dir+fs.name+'.squash'	  
                    #commands.getoutput(st)
                    commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                    commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                elif (struct_firmware.compression==1 or struct_firmware.compression==4):
                    
                    #st="./Squashfs/squashfs-all/unsquashfs/unsquashfs_xz_4.0 " + "-f -d "+ patth_dir+"/FS" + str(i) +" "+patth_dir+fs.name+'.squash'
                    
                    #commands.getoutput(st)
                    commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	  
                    commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                else: 
                    return -1         
            if (struct_firmware.s_major==3):
                commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
            i+=1

    i=1
    for fs in f1:
        with open(patth_dir+fs.name, 'rb+',0) as destination1, closing(mmap.mmap(destination1.fileno(), 0, access=mmap.ACCESS_READ)) as s:
            file=destination1
            buff=destination1.read()
            big_little=""
            for ij in pattern:
                
                start=s.find(ij[0])
                if start>=0:
                    big_little=ij[1]
                    break            
            struct_firmware=None
            end, struct_firmware=end_of_sqashfs(destination1,start,big_little)
            catch_buff=buff[start:(start+end)]
            if (fs.name.find("(")>=0):
                fs.name = fs.name[0:fs.name.find("(")]
            catch_squashfs_file=open(patth_dir+fs.name+'.squash', 'wb+')
            catch_squashfs_file.write(catch_buff)
            catch_squashfs_file.close()
            st=""
            if (struct_firmware.s_major==4):
                if (struct_firmware.compression==2):
                    #st="./Squashfs/squashfs-all/unsquashfs/unsquashfs_lzma_4.0 " + "-f -d "+ patth_dir+"/FS" + str(i) +" " +patth_dir+fs.name+'.squash'	  
                    #commands.getoutput(st)
                    commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                    commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                elif (struct_firmware.compression==1 or struct_firmware.compression==4):
                    
                    #st="./Squashfs/squashfs-all/unsquashfs/unsquashfs_xz_4.0 " + "-f -d "+ patth_dir+"/FS" + str(i) +" "+patth_dir+fs.name+'.squash'
                    
                    #commands.getoutput(st)  
                    commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                    commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                else: 
                	commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                    #return -1         
            if (struct_firmware.s_major==3):
                #commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
                commands.getoutput("./Squashfs/sasquatch-master/squashfs4.3/squashfs-tools/sasquatch " + "-f -d "+ patth_dir+"/FS" +str(i) +" "+patth_dir+fs.name+'.squash')  	
            i+=1


    foolder = []
    foold_all = []
    all_expansion1 = [['js',[]],['bin',[]],['sh',[]],['py',[]],['txt',[]],['other',[]]]
    all_expansion2 = [['js',[]],['bin',[]],['sh',[]],['py',[]],['txt',[]],['other',[]]]
    for j in range(2):
        for z in os.walk(patth_dir+"/FS" + str(j)):
            foolder.append(z)
           
               
        foold_all.append(foolder)
        foolder = []
    
        ##Здесь начинается блок в котором выбирабтся элементы для скриптов.... foold_all - все для 1 и 2 прошивки
    buf = []
         #проход по списку папки 1 и 2
    for t in foold_all[0]: # список файлов и папок для 1 ФС
            for filname in t[2]: # проход по именам файлов в папке
                flag=0
                for xx in all_expansion1:
                    if (filname.find('.'+xx[0])>0):
                        buf=[filname,t[0]] # имя файла, путь
                        xx[1].append(buf)
                        buf=[]
                        flag=1
                        

                if (flag==0): 
#---------------------------------------------------------------------
                    if ((m.file(t[0]+"/"+filname)[0:5]).find('ELF')>=0):
                        buf=[filname,t[0]]
                        all_expansion1[1][1].append(buf)
                        buf=[]
                        
                    
                else:
                    buf=[filname,t[0]]	
                    all_expansion1[5][1].append(buf) 
                    flag = 0
    for t in foold_all[1]: # список файлов и папок для 1 ФС
            for filname in t[2]: # проход по именам файлов в папке
                flag=0
                for xx in all_expansion2:
                    if (filname.find('.'+xx[0])>0):
                        buf=[filname,t[0]] # имя файла, путь
                        xx[1].append(buf)
                        buf=[]
                        flag=1
                        
                if (flag==0): 
#--------------------------------------------------------------------
                    if ((m.file(t[0]+"/"+filname)[0:5]).find('ELF')>=0):
                        buf=[filname,t[0]]
                        all_expansion2[1][1].append(buf)
                        buf=[]
                        
                    
                else:
                    buf=[filname,t[0]]	
                    all_expansion2[5][1].append(buf) 
                    flag = 0
    dif_files1=[]
    dif_files2=[]
    dif_files_buf=[]
    print all_expansion1[5][1]
    print all_expansion2[5][1]
    for index in range(min([len(all_expansion1),len(all_expansion2)])):
        tr1=[x[0] for x in all_expansion1[index][1]]
        tr2=[x[0] for x in all_expansion2[index][1]]
        for kk in tr1:
            flag=0
            for ss in tr2:
                if(ss==kk):
                    flag=1
                    break
            if (flag==0):
                dif_files_buf.append(kk)
                   
            else: flag=0
        dif_files1.append(dif_files_buf)# Есть в FS0, но нет в FS1
        dif_files_buf=[]

    tr1=[]
    tr2=[]
    

    for index in range(len(all_expansion1)):
        tr1=[x[0] for x in all_expansion1[index][1]]
        tr2=[x[0] for x in all_expansion2[index][1]]
        for kk in tr2:
            flag=0
            for ss in tr1:
                if(ss==kk):
                    flag=1
                    break
            if (flag==0):
                dif_files_buf.append(kk)
                   
            else: flag=0
        dif_files2.append(dif_files_buf)# Есть в FS0, но нет в FS1
        dif_files_buf=[]

    
    os.mkdir(patth_dir+"/bin")
    os.mkdir(patth_dir+"/bin/FS0")
    os.mkdir(patth_dir+"/bin/FS1")
    os.mkdir(patth_dir+"/script")
    os.mkdir(patth_dir+"/script/FS0")
    os.mkdir(patth_dir+"/other")
    os.mkdir(patth_dir+"/other/FS0")

    os.mkdir(patth_dir+"/script/FS1")
    os.mkdir(patth_dir+"/html")
    os.mkdir(patth_dir+"/html/FS0")
    os.mkdir(patth_dir+"/html/FS1")
    os.mkdir(patth_dir+"/other/FS1")
    os.mkdir(patth_dir+"/configure")
    os.mkdir(patth_dir+"/configure/FS0")
    os.mkdir(patth_dir+"/configure/FS1")

    for t in foold_all[0]: # список файлов и папок для 1 ФС
        for filename in t[2]:
            if ((m.file(t[0]+"/"+filename))[0:20].find('link') == -1) and ((m.file(t[0]+"/"+filename))[0:20].find(r'special') == -1):
                fll=0
                for i in dif_files1:
                    if i.count(filename)!=0:
                        fll=1
                        print filename
                        break
                if fll==1:
                    fll=0
                    continue	
                if ((m.file(t[0]+"/"+filename)[0:5]).find('ELF')>=0):	
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/bin/FS0")
                elif ((m.file(t[0]+"/"+filename)[0:6]).find('HTML')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/html/FS0")
                elif (filename.find('.js')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/script/FS0")
                elif (filename.find('.sh')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/script/FS0")
                elif (filename.find('.conf')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/configure/FS0")
                else:
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/other/FS0")

    for t in foold_all[1]: # список файлов и папок для 1 ФС
        for filename in t[2]:
            if ((m.file(t[0]+"/"+filename))[0:20].find('link') == -1) and ((m.file(t[0]+"/"+filename))[0:20].find(r'special') == -1):
                fll=0
                for i in dif_files2:
                    if i.count(filename)!=0:
                        fll=1
                        print filename
                        break
                if fll==1:
                    fll=0    
                    continue
                if ((m.file(t[0]+"/"+filename)[0:5]).find('ELF')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/bin/FS1")
                elif ((m.file(t[0]+"/"+filename)[0:5]).find('HTML')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/html/FS1")
                elif (filename.find('js')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/script/FS1")
                elif (filename.find('.sh')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/other/FS1")
                elif (filename.find('.conf')>=0):
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/configure/FS1")
                else:
                    shutil.copy2(t[0]+"/"+filename, patth_dir+"/other/FS1")
            
    #print dif_files1
    #print all_expansion2[0][1]
    #print all_expansion2[1][1] # ['js',[[имя,путь],...]..]
#def sort_file(path_dir):





                    	



def loadfw(request):
    return render(request, 'loadfirmware/loadfw.html', )

def upload_file(request):
 

    ip = 'http://185.17.3.240:8000/fwrequest/'
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print form.cleaned_data.get('Select_functions')
            if (str(request.session.session_key)!='None'):
                path_dir='/tmp/Django_files/'+str(request.session.session_key)+'/'
            else:
                path_dir='/tmp/Django_files/'+str(random.randint(0, 1000))+'/'	
            
            os.mkdir(path_dir)
            handle_uploaded_file(path_dir,request.FILES.getlist('file'), request.FILES.getlist('file1'), request.FILES.getlist('filename'))

            

            os.mkdir(path_dir+"/result")
            os.mkdir(path_dir+"/result/bin")
            os.mkdir(path_dir+"/result/html")
            os.mkdir(path_dir+"/result/configure")
            os.mkdir(path_dir+"/result/script")
            os.mkdir(path_dir+"/result/other")

            #Поиск различных файлов!

            file_diff = os.listdir(path_dir+'/bin/FS0')
            for i in file_diff:
                if (CRC32_from_file(path_dir+'/bin/FS0/'+i)==CRC32_from_file(path_dir+'/bin/FS1/'+i)):
                    os.remove(path_dir+'/bin/FS0/'+i)
                    os.remove(path_dir+'/bin/FS1/'+i)    
                
            file_diff = os.listdir(path_dir+'/html/FS0')
            for i in file_diff:
                if (CRC32_from_file(path_dir+'/html/FS0/'+i)==CRC32_from_file(path_dir+'/html/FS1/'+i)):
                    os.remove(path_dir+'/html/FS0/'+i)
                    os.remove(path_dir+'/html/FS1/'+i)
                else:
                    subprocess.call("diff -y -B -b -w --suppress-common-lines " + path_dir+'/html/FS0/'+i +" " + path_dir+'/html/FS1/'+i + " " + ">> " + path_dir+"/result/html/"+i, shell=True)	
                    
            file_diff = os.listdir(path_dir+'/configure/FS0')
            for i in file_diff:
                if (CRC32_from_file(path_dir+'/configure/FS0/'+i)==CRC32_from_file(path_dir+'/configure/FS1/'+i)):
                    os.remove(path_dir+'/configure/FS0/'+i)
                    os.remove(path_dir+'/configure/FS1/'+i)
                else:
                    subprocess.call("diff -y -B -b -w --suppress-common-lines " + path_dir+'/configure/FS0/'+i +" " + path_dir+'/configure/FS1/'+i + " " + ">> " + path_dir+"/result/configure/"+i, shell=True)   

            file_diff = os.listdir(path_dir+'/script/FS0')
            for i in file_diff:
                if (CRC32_from_file(path_dir+'/script/FS0/'+i)==CRC32_from_file(path_dir+'/script/FS1/'+i)):
                    os.remove(path_dir+'/script/FS0/'+i)
                    os.remove(path_dir+'/script/FS1/'+i)
                else:
                    subprocess.call("diff -y -B -b -w --suppress-common-lines " + path_dir+'/script/FS0/'+i +" " + path_dir+'/script/FS1/'+i + " " + ">> " + path_dir+"/result/script/"+i, shell=True)   

            file_diff = os.listdir(path_dir+'/other/FS0')
            for i in file_diff:
                if (CRC32_from_file(path_dir+'/other/FS0/'+i)==CRC32_from_file(path_dir+'/other/FS1/'+i)):
                    os.remove(path_dir+'/other/FS0/'+i)
                    os.remove(path_dir+'/other/FS1/'+i)
                else:
                    subprocess.call("diff -y -B -b -w --suppress-common-lines " + path_dir+'/other/FS0/'+i +" " + path_dir+'/other/FS1/'+i + " " + ">> " + path_dir+"/result/other/"+i, shell=True)   
   

            #сервер--------------------------
            aavv = os.listdir(path_dir+'bin/FS0')

            r = requests.get(ip,params={'key1': 'start'})
            r = requests.post(ip, json= form.cleaned_data.get('Select_functions'))
            for i in aavv:
                files1 = {'file': open(path_dir+'bin/FS0/'+i, 'rb'), }
                #multiple_files = [('binarys', ('tc1', open(path_dir+'bin/FS0/tc', 'rb'),'binarys/bin')), ('binarys', ('tc2', open(path_dir+'bin/FS1/tc','rb'),'binarys/bin'))]
                payload1 = {'key1': 'first', 'filename':i }
                r = requests.get(ip, params=payload1 )
                r = requests.post(ip, files=files1 )
                files2 = {'file': open(path_dir+'bin/FS1/'+i, 'rb'), }
                payload2 = {'key1': 'second', 'filename': i }
                r = requests.get(ip, params=payload2 )
                r = requests.post(ip, files=files2 )
                file = open(path_dir+"/result/bin/"+i, "w+")
                file.write(r.text)
                file.close()
            
            #конец сервера---------------------
            
            list_script=[]
            list_html=[]
            list_configure=[]
            list_binary=[]
            list_other=[]

            file_diff = os.listdir(path_dir+'/result/script/')
            for i in file_diff:
                a = open(path_dir+'/result/script/' + i, 'r+')
                bufread=a.read()
                list_script.append([i,bufread])
                a.close()

            file_diff = os.listdir(path_dir+'/result/html/')
            for i in file_diff:
                a = open (path_dir+'/result/html/' + i, "r+")
                bufread=a.read()
                list_html.append([i,bufread])
                a.close()

            file_diff = os.listdir(path_dir+'/result/configure/')
            for i in file_diff:
                a = open (path_dir+'/result/configure/' + i, "r+")
                bufread=a.read()
                list_configure.append([i,bufread])
                a.close()

            file_diff = os.listdir(path_dir+'/result/other/')
            for i in file_diff:
                a = open (path_dir+'/result/other/' + i, "r+")
                bufread=a.read()
                list_other.append([i,bufread])
                a.close()
            file_diff = os.listdir(path_dir+'/result/bin/')
            list_all_binary = []
            for i in file_diff:
                str_split = []
                add_buf=[]
               
                if os.path.getsize(path_dir+'/result/bin/' + i) == 0:
                    os.remove(path_dir+'/result/bin/' + i)
                else:
                   	
                
                    a=open(path_dir+'/result/bin/' + i)
                    valnerability_function = ''
                    zzzz=0

                    #for line in a:
                    #    print line	
                    #    if re.match('---\w*---', line) != None:
                            
                    #        if zzzz==0:
                    #            zzzz=1
                    #            valnerability_function = line[3:-4]
                    #            continue
                    #        else:
                    #            list_binary.append([valnerability_function, add_buf])
                    #            valnerability_function = line[3:-3]
                    #            add_buf=[]
                    #    else:
                    #        str_split = line.split(' ')

                    #        if str_split[0]==str_split[1] and str_split[2]=='0':
                    #            continue
                    #        else:
                    #            add_buf.append(str_split)
                    #list_binary.append([valnerability_function, add_buf])
                    #list_all_binary.append([i, list_binary])
                    
                    count1 = 0
                    for line in a:	
                        if re.match('---\w*---', line) != None:
                            count1+=1
                            valnerability_function = line[3:-4]
                            add_buf.append([valnerability_function,[]])
                        else:
                            str_split = line.split(' ')
                            if (str_split[0]==str_split[1]) and str_split[2]=='0\n':
                                continue
                            else:	
                                add_buf[int(count1-1)][1].append(str_split)
                    list_all_binary.append([i,add_buf])


            
            #shutil.rmtree(path_dir, ignore_errors=True)
            return render(request, 'loadfirmware/viwer.html', {'list_script': list_script, 'list_html':list_html, 'list_configure':list_configure, 'list_other':list_other, 'list_all_binary':list_all_binary})
        else:
            print str(request.FILES.getlist('filename'))	
    else:
        form = UploadFileForm()
    
   
    return render(request, 'loadfirmware/loadfw.html', {'form': form})