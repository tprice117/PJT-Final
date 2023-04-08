from django.forms import ModelForm
from .models import *
from django import forms


class ObjectForm(forms.ModelForm):
    class Meta:
        model = PrintFileStatus
        fields = ['PrintFileCompleted', 'OrderQuantityCompleted']
        


# class UserInfoForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()