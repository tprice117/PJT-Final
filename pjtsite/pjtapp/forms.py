from django.forms import ModelForm
from .models import *
from django import forms

from .models import UploadedFile


class ObjectForm(forms.ModelForm):
    class Meta:
        model = PrintFileStatus
        fields = ['PrintFileCompleted', 'OrderQuantityCompleted']
        

class UploadFileForm(forms.Form):
    file = forms.FileField()
# class UserInfoForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()