from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import *
from django.utils.translation import gettext as _

# Create your views here.
def home(request):
  OrderItemsList = list(OrderItems.objects.all())
  return render(request, 'home.html', {'OrderItemsList': OrderItemsList})

def uploadorders(request):
  return render(request, 'uploadorders.html')
  
def uploadprintdata(request):
  return render(request, 'uploadprintdata.html')
  
def details(request):
  return render(request, 'details.html')  

def summary(request):
  return render(request, 'summary.html')
# 2343347323	Shingo Sakurai	Shingo	Sakurai


# def OrderItems(request):
#   OrderItemsList = OrderItems.objects.all()
#   return render(request, 'home.html', {'OrderItemsList': OrderItemsList})