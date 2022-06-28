import csv, os, sys
sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import Orders, OrderItems, PrintModels
import numpy
import pandas as pd

def run():
  fhand = open('pjtapp/PJT-OrderItems.csv')
  
  reader = csv.reader(fhand)
  next(reader)
  
  OrderItems.objects.all().delete()

  for row in reader:
    print(row)

    o, created = Orders.objects.get_or_create(OrdersID=row[0])
    pm, created = PrintModels.objects.get_or_create(ModelSKU=row[1])

    oi = OrderItems(OrdersID=o, ItemSKU=pm, 
    OrderQuantity=row[2])
    oi.save()