from django.contrib import admin
from .models import Bill, Bills_Product, Client, Product
# Register your models here.

admin.site.register(Client)
admin.site.register(Bill)
admin.site.register(Bills_Product)
admin.site.register(Product)
