from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import *
from .models import OrderItems
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from scripts import orders_load
# Create your views here.

# class home(TemplateView):
#   template_name = 'home.html'
#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context["ordersSet"] = Orders.objects.all()
#       return context

def home(request):
  contextmap = {}
  contextmap["orderItemsSet"] = OrderItems.objects.all()
  contextmap["ordersSet"] = Orders.objects.all()
  # OrderItemsList = OrderItems.objects.all()
  # orderItems = OrderItems.objects.all()
  # orders = Orders.objects.all()
  return render(request, 'home.html', contextmap )
  
# return render(request, 'home.html', {'orderItems': orderItems, 'orders': orders} )
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