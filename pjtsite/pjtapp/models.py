# from typing_extensions import Required
from django.db import models
from django.forms import DecimalField

# Create your models here.
class OrderItems(models.Model):
  OrderID = models.CharField(max_length=32, primary_key=True) #Relationship with Orders is screwed up
  ItemSKU = models.CharField(max_length=48)
  OrderQuantity = models.CharField(max_length=12)

class Orders(models.Model): # Need to add OrderItemsID as PK and O2M to PrintFilestatus
  OrderID = models.ForeignKey(OrderItems, on_delete=models.CASCADE) #Relationship with OrderItems is screwed up
  FullName = models.CharField(max_length=48)
  FirstName = models.CharField(max_length=48)
  LastName = models.CharField(max_length=48)
  SaleDate = models.DateField()
  RequiredShipDate = models.DateField()
  OrderPlatform = models.CharField(max_length=32)
  OrderCompleted = models.BooleanField()



class PrintModels(models.Model): 
  ModelSkU = models.CharField(max_length=32, primary_key=True)
  ModelName = models.CharField(max_length=150)
  BoardGame = models.CharField(max_length=40)

class PrintFileData(models.Model): #Need to add PrintFileDataID
  ParentSKU = models.ForeignKey(PrintModels, on_delete=models.CASCADE)
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
  PrintFileStatusID = models.IntegerField(primary_key = True)
  OrderItemsID = models.IntegerField()
  ItemSKU = models.CharField(max_length=25)
  PrintFileID = models.IntegerField()
  OrderQuantityCompleted = models.IntegerField()
  PrintFileCompleted = models.BooleanField()

class PrintFileStateHistory(models.Model):
  PrintFileStateHistoryID = models.IntegerField()
  PrintFileStatusID = models.ForeignKey(PrintFileStatus, on_delete=models.CASCADE)
  StatusSetDate = models.DateField()
  StatusSetTime = models.TimeField()
  NewStateName = models.CharField(max_length=15)

class PrintFileStates(models.Model):
  PrintFileStatesID = models.IntegerField()
  StateName = models.CharField(max_length=15)

  def __str__(self):
    return self.OrderID