import csv, os, sys
sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import PrintFileData, PrintModels
import numpy
import pandas as pd
import logging


def run():
  fhand = open('pjtapp/PJT-PrintFileData.csv')

  reader = csv.reader(fhand)
  next(reader)

  #PrintFileData.objects.all().delete()

  for row in reader:
    print(row)
    pm, created = PrintModels.objects.get_or_create(ModelSKU=row[0])

    pfd = PrintFileData(FileName=row[1], Scope=row[2],
    Printer=row[3], Color=row[4], FileWeight=row[5],
    FileTime=row[6], PrintQuantity=row[7], PrintWeight=row[8],
    PrintTime=row[9], ParentSKU=pm)
    pfd.save()
    
def iterativeLoadPFD(PFDfile):
  fhand = PFDfile

  reader = csv.reader(PFDfile)
  next(reader)

  #PrintFileData.objects.all().delete()

  for row in reader:
    print(row)
    pm, created = PrintModels.objects.get_or_create(ModelSKU=row[0])

    pfd = PrintFileData(FileName=row[1], Scope=row[2],
    Printer=row[3], Color=row[4], FileWeight=row[5],
    FileTime=row[6], PrintQuantity=row[7], PrintWeight=row[8],
    PrintTime=row[9], ParentSKU=pm)
    pfd.save() 