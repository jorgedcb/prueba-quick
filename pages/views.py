from curses.ascii import HT
from inspect import Attribute
from itertools import product
from os import name
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from blog.models import Client, Bill, Product, Bills_Product
from .forms import CreateNewProduct

# Create your views here.
def home_view(request,*args,**kwargs): #home page view
    m = "jorge"
    return render(request, "main/home.html",{"name":m})

def all_products_view(request,*args,**kwargs): #Contact page view
    products = Product.objects.all()
  
    return render(request, "main/show_products.html", {"products":products})
    #return HttpResponse("<h1> %s </h1>") %(Cl.name, Product.id)

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


