# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import  DocumentForm
from .models import Voice
from django.http import HttpResponseRedirect
from django.contrib import messages
import sys, os, subprocess


# Create your views here.
def file_upload(request):
    return render(request,'voicerecognition/list.html',  {'form': DocumentForm})

def file_upload_final(request):
    if request.method == 'POST':
       form = DocumentForm(request.POST, request.FILES)
       file_name = str(request.FILES['docfile'])
       if form.is_valid():
          instance = Voice(docfile = request.FILES['docfile'])
          instance.user_id = request.user.id
          instance.save()
          path = os.path.abspath(str(instance.docfile.url))
          final_path= str(path).replace('/', '', 1)
          command = 'pocketsphinx_continuous -infile '+ final_path + ' > out.txt'
          print command, '************************************************************'
          res = os.system(command)
          fh = open("out.txt", "r")
          data =  str(fh.read())
          message = "The file has been uploaded"
          return render(request,'voicerecognition/final.html',  {'message':message,'data1':data})
       else:
           messages.error(request, form.errors)
    else:
         form = DocumentForm()
    return render(request,'voicerecognition/list.html',  {'form': DocumentForm})
