from django.db import models

# Create your models here.
class OrderItems(models.Model):
  OrderID = models.CharField(max_length=32)
  ItemSKU = models.CharField(max_length=48)
  OrderQuantity = models.CharField(max_length=12)
  
  def __str__(self):
    return self.OrderID