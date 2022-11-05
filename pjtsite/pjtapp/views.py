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
import numpy as np

orders = list(Orders.objects.filter(OrderCompleted=0).values())
orderitems = list(OrderItems.objects.values())
printmodels = list(PrintModels.objects.values())
printfiledata = list(PrintFileData.objects.values())

def home(request):
  # orders = list(Orders.objects.filter(OrderCompleted=0).values())
  # orderitems = list(OrderItems.objects.values())
  # printmodels = list(PrintModels.objects.values())
  # printfiledata = list(PrintFileData.objects.values())
  newOrderList=[]
  length = len(orders)

  for i in range(len(orders)):
    itemList = []
    RemPrintTime = 0
    order1 = {"FullName":orders[i]['FullName'], "OrdersID":orders[i]['OrdersID'], 
    "SaleDate":orders[i]['SaleDate'], "RequiredShipDate":orders[i]['RequiredShipDate']}

    for j in list(OrderItems.objects.filter(OrdersID_id = orders[i]['OrdersID']).values()):
      ModelName = PrintModels.objects.filter(ModelSKU = j['ItemSKU_id']).values_list('ModelName', flat=True).get()
      PrintWeight = list(PrintFileData.objects.filter(ParentSKU = j['ItemSKU_id']).values_list('PrintWeight', flat=True))
      PrintQuantity = list(PrintFileData.objects.filter(ParentSKU = j['ItemSKU_id']).values_list('PrintQuantity', flat=True))
      PrintTime = list(PrintFileData.objects.filter(ParentSKU = j['ItemSKU_id']).values_list('PrintTime', flat=True))
      FileTime = list(PrintFileData.objects.filter(ParentSKU = j['ItemSKU_id']).values_list('FileTime', flat=True))
      RemFiles = list(PrintFileStatus.objects.filter(tblOrderItems_ID_id = j['id'], PrintFileCompleted = 0).values_list('PrintFileCompleted', flat=True))
      RemFileSum = RemFiles.count(False)
      RemPrintTime = list(PrintFileData.objects.filter(ParentSKU = j['ItemSKU_id']).values_list('PrintTime', flat=True))
      RemPrintTime = sum(RemPrintTime)
      OrderQuantityCompleted = list(PrintFileStatus.objects.filter(tblOrderItems_ID_id = j['id']).values_list('OrderQuantityCompleted', flat=True))
      # RemTime = (sum(PrintQuantity) - sum(OrderQuantityCompleted)) * FileTime

      # RemTime = (PrintQuantity - sum(RemTime)) * list(PrintFileData.objects.filter(tblOrderItems_ID_id = j['id']).values_list('FileTime', flat=True))

      dictEntry = {
      'OrderSKU': j['ItemSKU_id'],
      'OrderQuantity': j['OrderQuantity'],
      'ModelName': ModelName,
      'PrintQuantity': PrintQuantity,
      'PrintWeight': PrintWeight,
      'PrintTime': PrintTime,
      'RemPrinttime': RemPrintTime,
      'RemFiles': RemFiles,
      'RemFileSum': RemFileSum}
      # 'RemTime': RemTime}

      if order1['OrdersID'] == 11461:
        exampleorder = order1
# , id = order1['OrdersID']
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
     'newOrderList' : newOrderList, 'printmodels': printmodels, 
     'exampleorder': exampleorder})
     
def uploadorders(request):
  return render(request, 'uploadorders.html')
  
def uploadprintdata(request):
  return render(request, 'uploadprintdata.html')
  
def details(request, orderid):
  newItemList=[]

  oid = None
  orderid_list = list(OrderItems.objects.filter(OrdersID_id = orderid).values())
  if len(orderid_list) > 0:
    oid = orderid_list[0]
  else: 
    oid = None
  for item in orderid_list:
    order_list = list(Orders.objects.filter(OrdersID = orderid).values())
    item_skus = OrderItems.objects.filter(OrdersID_id = item['OrdersID_id'], ItemSKU = item['ItemSKU_id']).values_list('ItemSKU_id', flat=True).get()
    item_name = PrintModels.objects.filter(ModelSKU = item['ItemSKU_id']).values_list('ModelName', flat=True).get()
    file_names = list(PrintFileData.objects.filter(ParentSKU = item['ItemSKU_id']).values_list('FileName', flat=True))
    file_colors = list(PrintFileData.objects.filter(ParentSKU = item['ItemSKU_id']).values_list('Color', flat=True))
    itemDictEntry = {
      'item_skus': item_skus,
      'item_name': item_name,
      'file_names': file_names,
      'file_colors': file_colors

    }
    newItemList.append(itemDictEntry)

  return render(request, 'details.html', {'oid': oid, 
  'order_list': order_list, "item_skus": item_skus, "orderid_list": orderid_list,
  'newItemList': newItemList})  

def summary(request):
  return render(request, 'summary.html')
# 2343347323	Shingo Sakurai	Shingo	Sakurai

# def OrderItems(request):
#   OrderItemsList = OrderItems.objects.all()
#   return render(request, 'home.html', {'OrderItemsList': OrderItemsList})