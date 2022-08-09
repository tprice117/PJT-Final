from pipes import Template
from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import *
from .models import OrderItems
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from scripts import orders_load
from django.views.generic import TemplateView, ListView
# Create your views here.

# class home(TemplateView):
#   template_name = 'home.html'
#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context["ordersSet"] = Orders.objects.all()
#       return context

# class homeListView(ListView):
#   template_name = 'home.html'
#   context_object_name = 'orders_list'
#   def get_queryset(self):
#     return Orders.objects.all()

def home(request):
  # contextmap = {}
  # contextmap["orderItemsSet"] = OrderItems.objects.select_related()
  # contextmap["ordersSet"] = Orders.objects.select_related()
  ojoinoi = OrderItems.objects.all()
  # orders = Orders.objects.all()
  return render(request, 'home.html', {'ojoinoi': ojoinoi})
  
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