import csv, os, sys
sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import Orders
import numpy
import pandas as pd

def run():
  fhand = open('pjtapp/PJT-Orders.csv')
  
  reader = csv.reader(fhand)
  next(reader)
  
  #Orders.objects.all().delete()

  for row in reader:
    print(row)
    df = pd.to_datetime(row[4])
    df2 = pd.to_datetime(row[5])
    # print(df)
    row[4] = df.strftime('%Y-%m-%d')
    row[5] = df2.strftime('%Y-%m-%d')
    row[7] = row[7].capitalize()
    o = Orders(OrdersID=row[0], FullName=row[1], FirstName=row[2],
     LastName=row[3], SaleDate=row[4], RequiredShipDate=row[5],
     OrderPlatform=row[6], OrderCompleted=row[7])
    o.save()


  # PrimID = models.AutoField(primary_key=True)
  # OrdersID = models.IntegerField(unique=True)
  # FullName = models.CharField(max_length=48)
  # FirstName = models.CharField(max_length=48)
  # LastName = models.CharField(max_length=48)
  # SaleDate = models.DateField()
  # RequiredShipDate = models.DateField()
  # OrderPlatform = models.CharField(max_length=32)
  # OrderCompleted = models.BooleanField()
  
def iterativeLoadO(Ofile):
    fhand = Ofile
  
    reader = csv.reader(fhand)
    next(reader)
    
    #Orders.objects.all().delete()

    for row in reader:
      print(row)
      df = pd.to_datetime(row[4])
      df2 = pd.to_datetime(row[5])
      # print(df)
      row[4] = df.strftime('%Y-%m-%d')
      row[5] = df2.strftime('%Y-%m-%d')
      row[7] = row[7].capitalize()
      o = Orders(OrdersID=row[0], FullName=row[1], FirstName=row[2],
      LastName=row[3], SaleDate=row[4], RequiredShipDate=row[5],
      OrderPlatform=row[6], OrderCompleted=row[7])
      o.save()