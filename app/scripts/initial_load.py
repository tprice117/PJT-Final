import csv, os, sys


from scripts import orderitems_load, orders_load, printfiledata_load, printmodels_load, printfilestatus_init
sys.path.append(os.path.dirname(os.getcwd()))
import datetime
from pjtapp.models import Orders, OrderItems, PrintModels, PrintFileData, PrintFileStatus
import numpy
import pandas as pd
import logging

def run():

  OrderItems.objects.all().delete()
  Orders.objects.all().delete()
  PrintFileData.objects.all().delete()
  PrintModels.objects.all().delete()
  PrintFileStatus.objects.all().delete()
  
  # print('orders')
  # orders_load.run()
  # print('printmodels')
  # printmodels_load.run()
  # print('orderitems')
  # orderitems_load.run()
  # print('printfiledata')
  # printfiledata_load.run()
  # print('printfilestatus')
  # printfilestatus_init.run()

