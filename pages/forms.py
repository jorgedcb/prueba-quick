from cProfile import label
import code
import imp
from os import name
from unittest.util import _MAX_LENGTH
from django import forms

class CreateNewClient(forms.Form):
    
    id = forms.IntegerField(label="id")
    document = forms.IntegerField(label="document")
    first_name = forms.CharField(label="first_name", max_length= 200)
    last_name = forms.CharField(label="last_name", max_length= 200)
    email = forms.EmailField(label="email", max_length= 200)

class CreateNewBill(forms.Form):
    
    id = forms.IntegerField(label="id")
    client_id = forms.IntegerField(label="client_id")
    company_name = forms.CharField(label="company name", max_length= 200)
    nit = forms.IntegerField(label="nit")
    code = forms.IntegerField(label="code")

class CreateNewBill_Product(forms.Form):
    
    id = forms.IntegerField(label="id")
    bill_id = forms.IntegerField(label="id")
    product_id = forms.IntegerField(label="id")
    
    

class CreateNewProduct(forms.Form):
    id = forms.IntegerField(label="id")
    name = forms.CharField(label="name", max_length= 200)
    description = forms.CharField(label="description", max_length= 200)
    attribute_4 = forms.CharField(label="attribute", max_length= 200)
