from dataclasses import fields
from django.forms import ModelForm
from .models import Product

class AddProdForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'