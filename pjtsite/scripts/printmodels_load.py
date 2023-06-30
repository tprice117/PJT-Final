import csv, os, sys
sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import PrintModels, OrderItems
import numpy
import pandas as pd
import logging

def run():
  logging.basicConfig(filename='printmodelsload.log', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
  fhand = open('pjtapp/PJT-PrintModels.csv', encoding='latin-1')
  #TODO:I have no idea why but i had to change encoding to latin-1 instead of utf-8 to stop an encoding exception 

  reader = csv.reader(fhand)
  next(reader)

  #PrintModels.objects.all().delete()

  for row in reader: 
    print(row)
    if PrintModels.ModelName != "":
      pm = PrintModels(ModelSKU=row[0], ModelName=row[1], BoardGame=row[2])
    else:
      logging.warning()
    #PrintModels.objects.filter(ModelSKU__isnull=True)

    pm.save()
    
def iterativeLoadPM(PMfile):
  logging.basicConfig(filename='printmodelsload.log', encoding='utf-8', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
  fhand = PMfile
  #TODO:I have no idea why but i had to change encoding to latin-1 instead of utf-8 to stop an encoding exception 

  reader = csv.reader(PMfile)
  next(reader)

  #PrintModels.objects.all().delete()

  for row in reader: 
    print(row)
    if PrintModels.ModelName != "":
      pm = PrintModels(ModelSKU=row[0], ModelName=row[1], BoardGame=row[2])
    else:
      logging.warning()
    #PrintModels.objects.filter(ModelSKU__isnull=True)

    pm.save()
    