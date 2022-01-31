"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from unicodedata import name
from xml.etree.ElementInclude import include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path


from pages import views

urlpatterns = [
    path('', views.home_view, name='home'), #path to home page
    path('admin/', admin.site.urls), #admin
    #clients
    path('client/<int:id>', views.client_view, name='client'), 
    path('client/all', views.all_clients_view, name='all client'),
    path('client/create/', views.create_client_view, name='create client'),

    #bills
    path('bill/<int:id>', views.bills_view, name='bill'), 
    path('bill/all', views.all_bills_view, name='all bill'),
    path('bill/create/', views.create_bill_view, name='create bill'),
    
    #bills_products
    path('billproduct/<int:id>', views.bills_products_view, name='bill_product'), 
    path('billproduct/all', views.all_bills_products_view, name='all bill_product'),
    path('billproduct/create/', views.create_bill_product_view, name='create bill_product'),


    #products
    path('product/<int:id>', views.product_view, name='product'), 
    path('product/all', views.all_products_view, name='all products'),
    path('product/create/', views.create_product_view, name='create product'),



]
