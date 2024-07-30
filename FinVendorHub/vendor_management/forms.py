from django import forms
from .models import Vendor, Product


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
