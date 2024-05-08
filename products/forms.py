from django import forms
from .models import ShoppingLists, Products


class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingLists
        fields = ('lists_name', 'products')

    products = forms.ModelMultipleChoiceField(
            queryset=Products.objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_name', )


