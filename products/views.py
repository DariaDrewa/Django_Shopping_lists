from django.shortcuts import redirect, render, get_object_or_404
from django.db import transaction
from django.http import HttpResponse
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Products, ShoppingLists
from django.template import loader


class ProductsListView(ListView):
    model = Products
    template_name = 'all_products.html'
    context_object_name = 'my_products'


class ShoppingListView(ListView):
    model = ShoppingLists
    template_name = 'all_shopping_lists.html'
    context_object_name = 'my_shopping_lists'


class ShoppingListDetails(DetailView):
    model = ShoppingLists
    template_name = "list_details.html"
    context_object_name = 'my_shopping_list'


class Main(generic.ListView):
    template_name = 'main.html'

    def get_queryset(self):
        qs1 = Products.objects.all()
        qs2 = ShoppingLists.objects.all()