from pipes import Template
from typing import OrderedDict
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.forms import formset_factory
from itertools import chain
from django.db.models import Count, Case, When
from django.db.models import Sum, IntegerField
from django.db.models.functions import Cast
from django.db.models import F
from django import forms, template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .models import OrderItems
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from scripts import orders_load
from django.views.generic import TemplateView, ListView, UpdateView
from django.db.models import Count, Sum, Avg
from .forms import ObjectForm
import numpy as np

orders = list(Orders.objects.filter(OrderCompleted=0).values())
orderitems = list(OrderItems.objects.values())
printmodels = list(PrintModels.objects.values())
printfiledata = list(PrintFileData.objects.values())
printfilestatus = list(PrintFileStatus.objects.values())

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
      # FileTime = list(PrintFileData.objects.filter(ParentSKU = j['ItemSKU_id']).values_list('FileTime', flat=True))
      RemFiles = list(PrintFileStatus.objects.filter(tblOrderItems_ID_id = j['id'], PrintFileCompleted = 0).values_list('PrintFileCompleted', flat=True))
      RemFileSum = RemFiles.count(False)
      

      RemPrintTime = PrintFileData.objects.filter(statuses__PrintFileCompleted = 0, statuses__ItemSKU = j['ItemSKU_id'],  statuses__tblOrderItems_ID_id = j['id']).aggregate(RemPrintTime=Sum('PrintTime')).get("RemPrintTime")

      # for l in list(PrintFileStatus.objects.filter(tblOrderItems_ID_id = j['id']).values()):
        
      #   RemPrintTime = list(PrintFileStatus.objects.select_related('tblPrintFileData_ID').all())
      # filter(id = l['tblPrintFileData_ID_id'], PrintFileCompleted = 0)
      # RemValues = list(PrintFileStatus.objects.filter(ItemSKU = j['ItemSKU_id']).values('PrintFileCompleted'))

      OrderQuantityCompleted = list(PrintFileStatus.objects.filter(tblOrderItems_ID_id = j['id']).values_list('OrderQuantityCompleted', flat=True))

      ColorCount = PrintFileData.objects.filter(statuses__tblOrderItems_ID_id = j['id']).values('Color').annotate(count=Count('Color'), weightSum = Sum('PrintWeight'), timeSum = Sum('PrintTime'),).order_by()
      RemVals = PrintFileData.objects.filter(statuses__tblOrderItems_ID_id = j['id']).values('Color').annotate(RemQuant = Sum(F('PrintQuantity') - F('statuses__OrderQuantityCompleted')), RemWeight = Sum((F('PrintQuantity') - F('statuses__OrderQuantityCompleted')) * F('PrintWeight')), RemTime = Sum((F('PrintQuantity') - F('statuses__OrderQuantityCompleted')) * F('PrintTime')))
      # RemQuant = PrintFileData.objects.filter(statuses__PrintFileCompleted__exact = 0, statuses__tblOrderItems_ID_id = j['id']).aggregate(RemQuant=Sum('PrintQuantity')).get("RemQuant")
      AllVals = zip(ColorCount, RemVals)
      # RemValues = PrintFileStatus.objects.filter(tbl
      # RemTime = (sum(PrintQuantity) - sum(OrderQuantityCompleted)) * FileTime
      # RemTime = (PrintQuantity - sum(RemTime)) * list(PrintFileData.objects.filter(tblOrderItems_ID_id = j['id']).values_list('FileTime', flat=True))
      # FileColor = PrintFileData.objects.filter(ParentSKU = j['ItemSKU_id']).values('Color', 'PrintQuantity', 'FileTime').order_by('Color')
      # FileCount = list(PrintFileData.objects.filter(Color = j[FileColor]).values_list('PrintQuantity', flat=True))
     
      dictEntry = {
      'OrderSKU': j['ItemSKU_id'],
      'OrderQuantity': j['OrderQuantity'],
      'ModelName': ModelName,
      'PrintQuantity': PrintQuantity,
      'PrintWeight': PrintWeight,
      'PrintTime': PrintTime,
      'RemPrinttime': RemPrintTime,
      'RemFiles': RemFiles,
      'RemFileSum': RemFileSum,
      'ColorCount': ColorCount,
      # 'RemQuant': RemQuant,
      'RemVals' : RemVals,
      'AllVals': AllVals,
      # 'LastValues': LastValues
      }
      # 'RemTime': RemTime}

      # if order1['OrdersID'] == 11461:
      #   exampleorder = order1
      itemList.append(dictEntry)
    order1['itemList'] = itemList
    newOrderList.append(order1)

  return render(request, 'home.html', {'orders' : orders,
   'orderitems' : orderitems,'order1' : order1,
    'itemList' : itemList, 'length' : length,
     'newOrderList' : newOrderList, 'printmodels': printmodels,})
    #  'exampleorder': exampleorder})
     
def uploadorders(request):
  return render(request, 'uploadorders.html')
  
def uploadprintdata(request):
  return render(request, 'uploadprintdata.html')
  
def details(request, orderid):
  # if request.method == "POST":
  #   print(request.POST)

  #   if request.POST.get("save"):
  #   for item in printfiledata.all():
  #     if request.POST.get()
  listCount = 0
  newItemList=[]
  oid = None
  orderid_list = list(OrderItems.objects.filter(OrdersID_id = orderid).values())
  if len(orderid_list) > 0:
    oid = orderid_list[0]
  else: 
    oid = None
  file_color_dict = {}
  for item in orderid_list:
    
    order_list = list(Orders.objects.filter(OrdersID = orderid).values())
    item_skus = OrderItems.objects.filter(OrdersID_id = item['OrdersID_id'], ItemSKU = item['ItemSKU_id']).values_list('ItemSKU_id', flat=True).get()
    item_name = PrintModels.objects.filter(ModelSKU = item['ItemSKU_id']).values_list('ModelName', flat=True).get()
    file_names = list(PrintFileData.objects.filter(ParentSKU = item['ItemSKU_id']).values_list('FileName', 'Color', 'FileWeight', 'FileTime', 'PrintQuantity', 'PrintWeight', 'PrintTime'))
    
    file_colors = list(PrintFileData.objects.filter(ParentSKU = item['ItemSKU_id']).values_list('Color', flat=True))
    pfsdata = list(PrintFileStatus.objects.filter(tblOrderItems_ID_id = item['id']).values())
    concList = zip(file_names, pfsdata)


    itemDictEntry = {
      'item_skus': item_skus,
      'item_name': item_name,
      'file_names': file_names,
      'file_colors': file_colors,
      'pfsdata' : pfsdata,
      'concList' : concList,
    }

    # file_color_dict[file_names].append(file_colors)
    newItemList.append(itemDictEntry)
  # for i in itemDictEntry[file_names]:
  #   file_color_dict[file_names]
  # CompletedFiles = request.POST['CompletedFiles']
  if request.method == "POST":
    # newFile = PrintFileStatus()
    nID = request.POST.get('fileID')
    #store new completed files in newFile
    nCompletedFiles = request.POST.get('CompletedFiles')

    newFile = PrintFileStatus.objects.get(id=nID)

    newFile.OrderQuantityCompleted = nCompletedFiles
    nPQuant = request.POST.get('PQuant')
    if nCompletedFiles >= nPQuant:
      newFile.PrintFileCompleted = True
    elif nCompletedFiles < nPQuant:
      newFile.PrintFileCompleted = False

    newFile.save()
    # if nCompletedFiles == 
    #retrieve all previous file objects
    


  return render(request, 'details.html', {'oid': oid, 
  'order_list': order_list, "item_skus": item_skus, "orderid_list": orderid_list,
  'newItemList': newItemList, 'printfilestatus': printfilestatus, 'pfsdata': pfsdata,
  'listCount': listCount})  



def detailsUpdate(request, filename):
  return render(request, 'detailsUpdate.html')



# def updateObject(request, pk):
#   object = PrintFileData.objects.get(id = pk)
#   form = ObjectForm(instance=object)
#   if request.method == 'POST':
#     form = ObjectForm(request.POST, instance=object)
#     if form.is_valid():
#       form.save()
#       return redirect('/')
#   context = {'form':form}
#   return render(request, 'details.html', context)
  
def details2(request):
  model = PrintFileData
  template_name = 'details2.html'
  fields = ['FileName']
  return render(request, 'details2.html')
# 2343347323	Shingo Sakurai	Shingo	Sakurai

# def OrderItems(request):
#   OrderItemsList = OrderItems.objects.all()
#   return render(request, 'home.html', {'OrderItemsList': OrderItemsList})
# def uploadorders(request):
#   if request.method == "POST":
#     form = UploadFileForm(request.POST, request.FILES)
#     if form.is_valid():
#       inst = ModelWithFileField(file_field = request.FILES["file"])
#       inst.save()
#     else:
#       form = UploadFileForm()
#   return render(request, 'uploadorders.html', {"form": form})

