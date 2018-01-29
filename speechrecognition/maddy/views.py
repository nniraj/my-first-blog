# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    data = Question.objects.values()
    return render(request,'maddy/index.html', {'data':data})

def save(request):
    print request.content_params
    return render(request,'maddy/result.html', {})

