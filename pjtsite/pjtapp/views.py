from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import OrderItems
from django.utils.translation import gettext as _

# Create your views here.
def home(request):
  OrderItemsList = list(OrderItems.objects.all())
  return render(request, 'home.html', {'OrderItemsList': OrderItemsList})

# def OrderItems(request):
#   OrderItemsList = OrderItems.objects.all()
#   return render(request, 'home.html', {'OrderItemsList': OrderItemsList})