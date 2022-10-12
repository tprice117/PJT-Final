from pipes import Template
from typing import OrderedDict
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django import template
from .models import *
from .models import OrderItems
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from scripts import orders_load
from django.views.generic import TemplateView, ListView
def home(request):
  orders = list(Orders.objects.filter(OrderCompleted=0).values())
  orderitems = list(OrderItems.objects.values())
  printmodels = list(PrintModels.objects.values())
  newOrderList=[]
  length = len(orders)
  for i in range(len(orders)):
    itemList = []

    order1 = {"FullName":orders[i]['FullName'], "OrdersID":orders[i]['OrdersID'], 
    "SaleDate":orders[i]['SaleDate'], "RequiredShipDate":orders[i]['RequiredShipDate']}
    for j in (list(OrderItems.objects.filter(OrdersID_id = orders[i]['OrdersID']).values())):
      dictEntry = {
      'OrderSKU': orderitems[i]['ItemSKU_id'],
      'OrderQuantity': orderitems[i]['OrderQuantity'],
      'ModelName': PrintModels.objects.filter(ModelSKU = orderitems[i]['ItemSKU_id']).values_list('ModelName', flat=True).get()}

      itemList.append(dictEntry)
    order1['itemList'] = itemList
    newOrderList.append(order1)

      # testList.append(printmodels[i]["ModelSKU"])
      # testList3.append(printmodels[j]["ModelSKU"])
      # testList2.append(dictEntry["OrderSKU"])

    # if (orderitems[i]["OrdersID_id"] == orders[i]["OrdersID"]):
    #   itemList.append(orderitems[i])

      
  #     {'FirstName': 'Shingo',
  #   'FullName': 'Shingo Sakurai',
  #   'LastName': 'Sakurai',
  #   'OrderCompleted': False,
  #   'OrderPlatform': 'Etsy',
  #   'OrdersID': 2343347323,
  #   'RequiredShipDate': datetime.date(2022, 1, 26),
  #   'SaleDate': datetime.date(2022, 1, 12)},

      # orders[i]["OrdersID"] = "h"
      # orderid = orders[i]["OrdersID"]
      # if orderitems[i] == orders[i]["OrdersID"]:
      #   orderitems = orderitems.filter(OrdersID__exact=orders[i]["OrdersID"])
      # orders[i]["items"] = orderitems[i]

      # if orderitems[i] == orders[i]["OrdersID"]:
      #   orders[i]["items"] = OrderItems[i]
      # if orders[i]["OrdersID"] == orderitems["OrdersID_id"]:
      #   orders[i]["items"] = orderitems
      # if (orders[i]["OrdersID"] == 10761):
      #   orders[i]["OrdersID"] = "f"

  return render(request, 'home.html', {'orders' : orders,
   'orderitems' : orderitems,'order1' : order1,
    'itemList' : itemList, 'length' : length,
     'newOrderList' : newOrderList, 'printmodels': printmodels})
     
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