from django.shortcuts import redirect, render, get_object_or_404
from django.db import transaction
from django.http import HttpResponse
from django.views.generic.list import ListView, View
from django.views.generic.detail import DetailView
from django.template import loader
from .models import Products, ShoppingLists


class ProductsListView(ListView):
    model = Products
    template_name = 'all_products.html'
    my_products = Products.objects.all().values()
    context_object_name = 'my_products'


class ShoppingListView(ListView):
    model = ShoppingLists
    template_name = 'all_shopping_lists.html'
    my_shopping_lists = ShoppingLists.objects.all()
    context_object_name = 'my_shopping_lists'


class ShoppingListDetails(DetailView):
    model = ShoppingLists
    template_name = "list_details.html"


#    model = ShoppingLists
#    template_name = 'list_details.html'
#    context_object_name = 'my_shopping_list'


#@transaction.atomic
#def add(request, products_id):
#   products = shopping_list.objects.get(id=products_id)
#   rez = shopping_list(products=products)
#   rez.save()
#   return redirect("")

#@transaction.atomic
#def delete(request, products_id):
#    try:
#        rez = Rezerwacja.objects.get(id=rezerwacja_id)
#    except Rezerwacja.DoesNotExist:
#        pass
#    else:
#        rez.delete()
#    return redirect("index")

