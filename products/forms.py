from django import forms
from .models import ShoppingLists, Products





class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingLists
        fields = ('lists_name', 'products')


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_name', )


class QuantityInput(forms.ModelForm):
    class Meta:
        model = ShoppingLists
        fields = ('quantity', )