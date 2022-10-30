import csv, os, sys

sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import PrintFileData, PrintFileStatus
import numpy
import pandas as pd
import logging
from pjtapp.models import Orders, OrderItems, PrintModels

def run():
  orderitems = list(OrderItems.objects.values())
  printfiledata = list(PrintFileData.objects.values())
  #PrintFileData.objects.filter(ParentSKU = orderitems[row]['ItemSKU_id']).values_list('ParentSKU', flat=True).get()

  for row in range(len(orderitems)):
    print(row)
    oi = orderitems[row]['id']
    qspfd = PrintFileData.objects.filter(ParentSKU = orderitems[row]['ItemSKU_id']).values_list()
    for rec in range(len(qspfd)):
    # for rec in range(len(printfiledata)):
      # oisku, created = OrderItems.objects.get(ItemSKU = i[1])
      pfs = PrintFileStatus(
      ItemSKU = orderitems[rec]['ItemSKU_id'],
      OrderQuantityCompleted = 0,
      PrintFileCompleted = 0,
      tblOrderItems_ID_id = oi,
      tblPrintFileData_ID_id = printfiledata[rec]['id']
      ) 
      pfs.save()