# -*-coding:utf-8-*-

from django.forms import ModelForm
from django import forms
from .models import Voice

class DocumentForm(ModelForm):
    class Meta:
        model = Voice
        fields = ('docfile', 'user',)

    def clean_docfile(self):
        check_list = ['wav', 'mp3']
        data = str(self.cleaned_data['docfile'])
        data = data.split('.')
        if data[len(data)-1] not in check_list:
            raise forms.ValidationError('This format is not valid. Please ensure that you have file with wav or mp3 format')
        return data
