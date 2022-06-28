# from typing_extensions import Required
from tkinter import CASCADE
from django.db import models
from django.forms import DecimalField

# Create your models here.

class Orders(models.Model):
  # PrimID = models.AutoField(primary_key=True)
  OrdersID = models.BigIntegerField(primary_key= True, unique=True)
  FullName = models.CharField(max_length=48)
  FirstName = models.CharField(max_length=48)
  LastName = models.CharField(max_length=48)
  SaleDate = models.DateField()
  RequiredShipDate = models.DateField() #DATE FORMATS NOT ACCEPTED IN MODEL VERSION BUT IN FORMAT IS FINE
  OrderPlatform = models.CharField(max_length=32)
  OrderCompleted = models.BooleanField()

class PrintModels(models.Model): 
  # ModelID = models.AutoField(primary_key=True)
  ModelSKU = models.CharField(primary_key=True, max_length=24, unique=True)
  ModelName = models.CharField(max_length=150)
  BoardGame = models.CharField(max_length=40)

class OrderItems(models.Model):
  # OrderItemsID = models.AutoField(primary_key=True) 
  OrdersID = models.ForeignKey(Orders, to_field="OrdersID", db_column="OrdersID", on_delete=models.CASCADE)
  ItemSKU = models.ForeignKey(PrintModels, to_field="ModelSKU", db_column="ItemSKU", on_delete=models.CASCADE)
  OrderQuantity = models.CharField(max_length=12)

class PrintFileData(models.Model): #Need to add PrintFileDataID
  # PrintFileDataID = models.AutoField(primary_key = True)
  ParentSKU = models.ForeignKey(PrintModels, to_field="ModelSKU", db_column="ParentSKU", on_delete=models.CASCADE)
  FileName = models.CharField(max_length=128)
  Scope = models.CharField(max_length=48)
  Printer = models.CharField(max_length=48)
  Color = models.CharField(max_length=48)
  FileWeight = models.IntegerField()
  FileTime = models.DecimalField(max_digits=5, decimal_places=2)
  PrintQuantity = models.IntegerField()
  PrintWeight = models.IntegerField()
  PrintTime = models.DecimalField(max_digits=5, decimal_places=2)

class PrintFileStatus(models.Model):
  # PrintFileStatusID = models.AutoField(primary_key = True)
  tblOrderItems_ID = models.ForeignKey(OrderItems, on_delete=models.CASCADE)
  ItemSKU = models.CharField(max_length=25)
  tblPrintFileData_ID = models.ForeignKey(PrintFileData, on_delete=models.CASCADE)
  OrderQuantityCompleted = models.IntegerField()
  PrintFileCompleted = models.BooleanField()

class PrintFileStateHistory(models.Model):
  # PrintFileStateHistoryID = models.AutoField(primary_key = True)
  PrintFileStatusID = models.ForeignKey(PrintFileStatus, on_delete=models.CASCADE)
  StatusSetDate = models.DateField()
  StatusSetTime = models.TimeField()
  NewStateName = models.CharField(max_length=15)

class PrintFileStates(models.Model):
  # PrintFileStatesID = models.AutoField(primary_key = True)
  StateName = models.CharField(max_length=15)

  def __str__(self):
    return self.OrderID