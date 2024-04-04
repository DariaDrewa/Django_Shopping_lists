from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Products, ShoppingLists, ShoppingListForm
from django.http import request

class ProductsListView(ListView):
    model = Products
    template_name = 'all_products.html'
    context_object_name = 'my_products'


class ShoppingListView(ListView):
    model = ShoppingLists
    template_name = 'all_shopping_lists.html'
    context_object_name = 'my_shopping_lists'

    def get_context_data(self, **kwargs):
        context = super(ShoppingListView, self).get_context_data(**kwargs)
        context["form"] = ShoppingListForm(self.request.POST or None)
        return context
    def post(self, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        form = context["form"]
        if form.is_valid():
            lists_name = self.request.POST["lists_name"]

            if lists_name != "":
                self.object_list = self.object_list.filter(lists_name=lists_name)

            context[self.context_object_name] = self.object_list
        return render(self.request, self.template_name, context)

class ShoppingListDetails(DetailView):
    model = ShoppingLists
    template_name = "list_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_list'] = Products.objects.filter(shoppinglists=self.object.id)
        return context


class Main(generic.ListView):
    template_name = 'main.html'

    def get_queryset(self):
        qs1 = Products.objects.all()
        qs2 = ShoppingLists.objects.all()


def shopping_list_create(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list = form.save()
            return redirect('details', shopping_list.pk)
    else:
        form = ShoppingListForm

    return render(request,
                  'new_shopping_list.html',
                  {'form': form})


def shopping_list_change(request, id):
    shoppinglist = ShoppingLists.objects.get(id=id)
    if request.method == 'POST':
        form = ShoppingListForm(request.POST, instance=shoppinglist)
        if form.is_valid():
            form.save()
            return redirect('details', shoppinglist.id)
    else:
        form = ShoppingListForm(instance=shoppinglist)

    return render(request,
                  'shopping_list_change.html',
                  {'shoppinglist': shoppinglist,
                   'form': form})


def shopping_list_delete(request, id):
    shoppinglist = ShoppingLists.objects.get(id=id)
    if request.method == "POST":
        shoppinglist.delete()
        return redirect('shopping_list')

    return render(request,
                  'delete_confirmation_page_list.html',
                  {'shoppinglist': shoppinglist})
