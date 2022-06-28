## DO NOT RUN THIS THIS IS A TEST PYTHON SCRIPT ##
## FOR DEVELOPMENT PURPOSES ##

import csv, os, sys
sys.path.append(os.path.dirname(os.getcwd()))
from datetime import datetime
import numpy

import pandas as pd
format_date = '%y/%d/%m'
print(os.getcwd())
# fhand = open('pjtsite/pjtapp/PJT-Orders.csv')
fhand = open('pjtsite/pjtapp/PJT-OrderItems.csv')
reader = csv.reader(fhand)
next(reader)

for row in reader:
  # print (row[4], row[5])
  # df = pd.to_datetime(row[4])
  # df2 = pd.to_datetime(row[5])
  # # print(df)
  # row[4] = df.strftime('%Y-%m-%d')
  # row[5] = df2.strftime('%Y-%m-%d')
  # print(row[4])
  # print(row[5])
  print(row[2])

