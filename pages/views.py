from curses.ascii import HT
from http import client
from importlib.util import find_spec
from inspect import Attribute
from itertools import product
from os import name
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from blog.models import Client, Bill, Product, Bills_Product
from .forms import CreateNewClient, CreateNewProduct

# Create your views here.
def home_view(request,*args,**kwargs): #home page view
    m = "jorge"
    return render(request, "main/home.html",{"name":m})

def all_products_view(request,*args,**kwargs): #Contact page view
    products = Product.objects.all()
  
    return render(request, "main/show_products.html", {"products":products})

def product_view(request,*args,**kwargs): #Contact page view
    product = Product.objects.get(id=kwargs['id'])
    return render(request, "main/product.html", {"product":product})
    

def create_product_view(request,*args,**kwargs):
    if request.method == "POST":
        form = CreateNewProduct(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            attribute_4 = form.cleaned_data["attribute_4"]

            t = Product(id=id, name=name, description=description, attribute_4=attribute_4)
            t.save()

        return HttpResponseRedirect("/product/all")
    else:
        form = CreateNewProduct()

    return render(request, "main/create_product.html", {"form":form})

def all_clients_view(request,*args,**kwargs): #Contact page view
    clients = Client.objects.all()
    return render(request, "main/show_clients.html", {"clients":clients})

def client_view(request,*args,**kwargs): #Contact page view
    print(kwargs)
    client = Client.objects.get(id=kwargs['id'])
    return render(request, "main/clients.html", {"client":client})

def create_client_view(request,*args,**kwargs):
    if request.method == "POST":
        form = CreateNewClient(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            document = form.cleaned_data["document"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]

            t = Client(id=id, document=document, first_name=first_name, last_name=last_name, email=email)
            t.save()

        return HttpResponseRedirect("/client/all")
    else:
        form = CreateNewClient()

    return render(request, "main/create_client.html", {"form":form})


