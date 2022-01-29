from cgitb import text
import email
from itertools import product
from pickle import TRUE
from pyexpat import model
from ssl import Options
from turtle import title
from unicodedata import name
from xml.dom.minidom import Document
from django.db import models
from django.conf import settings
from django.utils import timezone
#Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    

class Clients(models.Model):

    id = models.PositiveIntegerField(primary_key = TRUE)
    document = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    # def __str__(self):
    #     return self.first_name
    #     #return "%s %s" % (self.first_name, self.last_name)

class Bills(models.Model):
    
    id = models.PositiveIntegerField(primary_key = TRUE)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    nit = models.PositiveIntegerField()
    code = models.PositiveIntegerField()
    # def __str__(self):
    #     return self.id

class Products(models.Model):
    
    id = models.PositiveIntegerField(primary_key = TRUE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    attribute_4 = models.TextField()
    # def __str__(self):
    #     return self.name

class Bills_Products(models.Model):
    
    id = models.PositiveIntegerField(primary_key = TRUE)
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.id




