from django.forms import ModelForm
from .models import *


class ObjectForm(ModelForm):
    class Meta:
        model = PrintFileData
        fields = '__all__'