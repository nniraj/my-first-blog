# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=1024)
    opt1 = models.CharField(max_length=1024)
    opt2 = models.CharField(max_length=1024)
    opt3 = models.CharField(max_length=1024)
    opt4 = models.CharField(max_length=1024)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
