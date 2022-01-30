from curses.ascii import HT
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from blog.models import Client, Bill, Product, Bills_Product
from .forms import CreateNewProduct

# Create your views here.
def home_view(request,*args,**kwargs): #home page view
    m = "jorge"
    return render(request, "main/home.html",{"name":m})

def product_view(request,*args,**kwargs): #Contact page view
    print(args)
    print(kwargs) #id se pasa aca
    # Cl = Client.objects.get(id = id)
    return HttpResponse("<h1> Contact page </h1>")
    #return HttpResponse("<h1> %s </h1>") %(Cl.name, Product.id)

def create_product_view(response):
    form = CreateNewProduct()
    return render(response, "main/create_product.html", {"form": form}) # goes inside views.py
    


