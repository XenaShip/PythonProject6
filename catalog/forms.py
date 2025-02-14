from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductModerForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("description", "category")