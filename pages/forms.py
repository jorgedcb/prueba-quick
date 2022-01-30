from cProfile import label
import imp
from os import name
from unittest.util import _MAX_LENGTH
from django import forms

class CreateNewProduct(forms.Form):
    id = forms.IntegerField(label="id")
    name = forms.CharField(label="name", max_length= 200)
    description = forms.CharField(label="description", max_length= 200)
    attribute_4 = forms.CharField(label="attribute", max_length= 200)
