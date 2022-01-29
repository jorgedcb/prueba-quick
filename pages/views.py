from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs): #home page view
    return render(request, "home.html",{})

def contact_view(request,*args,**kwargs): #Contact page view
    return HttpResponse("<h1> Contact page </h1>") #string of HTML code

