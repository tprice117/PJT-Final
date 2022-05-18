from typing_extensions import Required
from django.db import models
from django.forms import DecimalField

# Create your models here.
class OrderItems(models.Model):
  OrderID = models.CharField(max_length=32)
  ItemSKU = models.CharField(max_length=48)
  OrderQuantity = models.CharField(max_length=12)

class Orders(models.Model):
  OrderID = models.CharField(max_length=32)
  FullName = models.CharField(max_length=48)
  FirstName = models.CharField(max_length=48)
  LastName = models.CharField(max_length=48)
  SaleDate = models.DateField()
  RequiredShipDate = models.DateField()
  OrderPlatform = models.CharField(max_length=32)
  OrderCompleted = models.BooleanField()

class PrintFileData(models.Model):
  SKU = models.CharField(max_length=32)
  FileName = models.CharField(max_length=128)
  Scope = models.CharField(max_length=48)
  Printer = models.CharField(max_length=48)
  Color = models.CharField(maxlength=48)
  FileWeight = models.IntegerField(max_length=12)
  FileTime = models.DecimalField(max_digits=5, decimal_places=2)
  PrintQuantity = models.IntegerField(max_length=12)
  PrintWeight = models.IntegerField(max_length=12)
  PrintTime = models.DecimalField(max_digits=5, decimal_places=2)

class PrintModels(models.Model):
  ModelSkU = models.CharField(max_length=32)
  ModelName = models.CharField(max_length=150)
  BoardGame = models.CharField(max_length=40)

class PrintFileStatus(models.Model):
  PrintFileStatusID = models.IntegerField(max_length=4)
  OrderItemsID = models.IntegerField(max_length=4)
  ItemSKU = models.CharField(max_length=25)
  PrintFileID = models.IntegerField(max_length=4)
  OrderQuantityCompleted = models.IntegerField(max_length=4)
  PrintFileCompleted = models.BooleanField()

class PrintFileStateHistory(models.model):
  PrintFileStateHistoryID = models.IntegerField(max_length=4)
  PrintFileStatusID = models.IntegerField(max_length=4)
  StatusSetDate = models.DateField()
  StatusSetTime = models.TimeField()
  NewStateName = models.CharField(max_length=15)

class PrintFileStates(models.model):
  PrintFileStatesID = models.IntegerField(max_length=4)
  StateName = models.CharField(max_length=15)

  def __str__(self):
    return self.OrderID