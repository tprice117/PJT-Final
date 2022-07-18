import csv, os, sys
from scripts import orderitems_load, orders_load, printfiledata_load, printmodels_load
sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import Orders, OrderItems, PrintModels, PrintFileData
import numpy
import pandas as pd
import logging

def run():

  OrderItems.objects.all().delete()
  Orders.objects.all().delete()
  PrintFileData.objects.all().delete()
  PrintModels.objects.all().delete()
  
  orders_load.run()
  printmodels_load.run()
  orderitems_load.run()
  printfiledata_load.run()
  

