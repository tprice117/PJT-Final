import csv, os, sys
sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import Orders, OrderItems, PrintModels
import numpy
import pandas as pd
import logging

def run():
  logging.basicConfig(filename='orderitemsload.log', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
  fhand = open('pjtapp/PJT-OrderItems.csv')
  
  reader = csv.reader(fhand)
  next(reader)

  #OrderItems.objects.all().delete()

  for row in reader:
    print(row)
    o, created = Orders.objects.get_or_create(OrdersID=row[0])
    pm, created = PrintModels.objects.get_or_create(ModelSKU=row[1])

    oi = OrderItems(OrdersID=o, ItemSKU=pm, 
    OrderQuantity=row[2])
    oi.save()
    
  if PrintModels.objects.filter(ModelName__exact=''):
    c = PrintModels.objects.filter(ModelName__exact='').values()
    print(c[1])
    for value in c.values():
      logging.warning(value)
    PrintModels.objects.filter(ModelName__exact='').delete()
    
def iterativeLoadOI(oifile):
  logging.basicConfig(filename='orderitemsload.log', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
  fhand = oifile
  
  reader = csv.reader(fhand)
  next(reader)

  #OrderItems.objects.all().delete()
  # Open the file in text mode
  with open(file_path, 'rt') as file:
    # Process the file and return text data
    for line in file:
        # Process each line of the file
        # ...
      print(row)
      o, created = Orders.objects.get_or_create(OrdersID=row[0])
      pm, created = PrintModels.objects.get_or_create(ModelSKU=row[1])

      oi = OrderItems(OrdersID=o, ItemSKU=pm, 
      OrderQuantity=row[2])
      oi.save()
        # Return the processed text data
      yield oi
        
    if PrintModels.objects.filter(ModelName__exact=''):
      c = PrintModels.objects.filter(ModelName__exact='').values()
      print(c[1])
      for value in c.values():
        logging.warning(value)
      PrintModels.objects.filter(ModelName__exact='').delete()