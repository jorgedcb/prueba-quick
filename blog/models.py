from cgitb import text
import email
from itertools import product
from pickle import TRUE
from pyexpat import model
from ssl import Options
from turtle import title
from typing_extensions import Self
from unicodedata import name
from xml.dom.minidom import Document
from django.db import models
from django.conf import settings
from django.utils import timezone
#Create your models here.


class Client(models.Model):

    id = models.PositiveIntegerField(primary_key = TRUE)
    document = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return "%s - %s %s" % (self.id,self.first_name, self.last_name)

class Bill(models.Model):
    
    id = models.PositiveIntegerField(primary_key = TRUE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    nit = models.PositiveIntegerField()
    code = models.PositiveIntegerField()
    def __str__(self):
        return "%s - %s" % (self.id, self.company_name)

class Product(models.Model):
    
    id = models.PositiveIntegerField(primary_key = TRUE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    attribute_4 = models.TextField()
    def __str__(self):
        return "%s - %s" % (self.id, self.name)


class Bills_Product(models.Model):
    
    id = models.PositiveIntegerField(primary_key = TRUE)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % (self.id)




