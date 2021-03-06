import csv, os, sys
sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import PrintModels, OrderItems
import numpy
import pandas as pd

def run():
  fhand = open('pjtapp/PJT-PrintModels.csv')

  reader = csv.reader(fhand)
  next(reader)

  PrintModels.objects.all().delete()

  for row in reader: 
    print(row)
    pm = PrintModels(ModelSKU=row[0], ModelName=row[1], BoardGame=row[2])
    pm.save()