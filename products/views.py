from django.shortcuts import redirect
from django.db import transaction
from django.http import HttpResponse
from django.template import loader
from .models import Products, ShoppingLists


def products(request):
    my_products = Products.objects.all().values()
    template = loader.get_template('all_products.html')
    context = {
        'my_products': my_products,
    }
    return HttpResponse(template.render(context, request))


def shopping_list(request):
    my_shopping_lists = ShoppingLists.objects.all().values()
    template = loader.get_template('all_shopping_lists.html')
    context = {
        'my_shopping_lists': my_shopping_lists,
    }
    return HttpResponse(template.render(context, request))


def list_details(request, id):
    my_shopping_list = ShoppingLists.objects.get(id=id)
    template = loader.get_template('list_details.html')
    context = {
        'my_shopping_list': my_shopping_list,
    }
    return HttpResponse(template.render(context, request))


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

