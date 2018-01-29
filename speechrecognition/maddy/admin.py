# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['text', 'opt1','opt2','opt3', 'opt4' ]


admin.site.register(Question,  QuestionAdmin)
