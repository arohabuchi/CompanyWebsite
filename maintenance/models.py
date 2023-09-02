from django.db import models

from inventory.models import Inventory
from django.contrib.auth.models import User

# Create your models here.
class maintenance(models.Model):
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    part_repaired= models.CharField(max_length=250)
    supervised_by=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    mechanic_Name = models.CharField(max_length=200, blank=True, null=True)
    mechanic_Number = models.CharField(max_length=200, blank=True, null=True)
    amount_spent = models.FloatField( blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True, null=True)
    
    is_completed = models.BooleanField(default=True)
    
    
    