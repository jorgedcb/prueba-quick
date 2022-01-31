from curses.ascii import HT
from http import client
from importlib.util import find_spec
from inspect import Attribute
from itertools import product
from os import name
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from blog.models import Client, Bill, Product, Bills_Product
from .forms import CreateNewBill, CreateNewBill_Product, CreateNewClient, CreateNewProduct

# Create your views here.
def home_view(request,*args,**kwargs): #home page view
    m = "jorge"
    return render(request, "main/home.html",{"name":m})

#products views

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
#client views
def all_clients_view(request,*args,**kwargs): #Contact page view
    clients = Client.objects.all()
    return render(request, "main/show_clients.html", {"clients":clients})

def client_view(request,*args,**kwargs): #Contact page view
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

#Bill views
def all_bills_view(request,*args,**kwargs): #Contact page view
    bills = Bill.objects.all()
    return render(request, "main/show_bills.html", {"bills":bills})

def bills_view(request,*args,**kwargs): #Contact page view
    bill = Bill.objects.get(id=kwargs['id'])
    return render(request, "main/bills.html", {"bill":bill})

def create_bill_view(request,*args,**kwargs):
    if request.method == "POST":
        form = CreateNewBill(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            client_id = form.cleaned_data["client_id"]
            company_name  = form.cleaned_data["company_name"]
            nit  = form.cleaned_data["nit"]
            code = form.cleaned_data["code"]
            client = Client.objects.get(id=client_id)


            t = Bill(id=id, client_id=client, company_name=company_name, nit=nit, code=code)
            t.save()

        return HttpResponseRedirect("/bill/all")
    else:
        form = CreateNewBill()

    return render(request, "main/create_bill.html", {"form":form})

#bill_product
def all_bills_products_view(request,*args,**kwargs): #Contact page view
    bills_products = Bills_Product.objects.all()
    return render(request, "main/show_billproduct.html", {"bills_products":bills_products})

def bills_products_view(request,*args,**kwargs): #Contact page view
    bill_product = Bills_Product.objects.get(id=kwargs['id'])
    return render(request, "main/bill_product.html", {"bill_product":bill_product})

def create_bill_product_view(request,*args,**kwargs):
    if request.method == "POST":
        form = CreateNewBill_Product(request.POST)
        if form.is_valid():
            id = form.cleaned_data["id"]
            bill_id = form.cleaned_data["bill_id"]
            product_id = form.cleaned_data["product_id"]

            bill= Bill.objects.get(id=bill_id)
            product = Product.objects.get(id=product_id)
            t = Bills_Product(id=id, bill_id=bill, product_id=product)
            t.save()

        return HttpResponseRedirect("/billproduct/all")
    else:
        form = CreateNewBill_Product()

    return render(request, "main/create_bill_product.html", {"form":form})



