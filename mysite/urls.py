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
    path('product/<int:id>', views.product_view, name='product'), #path to product page
    path('admin/', admin.site.urls),
    path('create/product', views.create_product_view, name='create product'),

]
