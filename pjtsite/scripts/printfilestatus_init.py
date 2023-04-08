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

  for row in orderitems:
    
    oi = row['id']
    print("new row", row, oi)
    qspfd = PrintFileData.objects.filter(ParentSKU = row['ItemSKU_id']).values()
    print(qspfd)

    for rec in qspfd:
      # if (row == 2):
      #   print(rec, 'id', qspfd[rec])
    # for rec in range(len(printfiledata)):
      # oisku, created = OrderItems.objects.get(ItemSKU = i[1])
      pfs = PrintFileStatus(
      ItemSKU = rec['ParentSKU_id'],
      OrderQuantityCompleted = 0,
      PrintFileCompleted = 0,
      tblOrderItems_ID_id = oi,
      tblPrintFileData_ID_id = rec['id']
      ) 
      pfs.save()