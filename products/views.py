from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from .models import Products, ShoppingLists
from .forms import ShoppingListForm, ProductsForm


class Main(generic.ListView):
    template_name = 'main.html'

    def get_queryset(self):
        qs1 = Products.objects.all()
        qs2 = ShoppingLists.objects.all()


class ProductsListView(ListView):
    model = Products
    template_name = 'all_products.html'
    context_object_name = 'my_products'

    def get_queryset(self):
        return Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context["form"] = ProductsForm(self.request.POST or None)
        return context

    def post(self, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        form = context["form"]
        if form.is_valid():
            product_name = self.request.POST["product_name"]

            if product_name != "":
                self.object_list = self.object_list.filter(product_name=product_name)

            context[self.context_object_name] = self.object_list
        return render(self.request, self.template_name, context)


class ShoppingListView(ListView):
    model = ShoppingLists
    template_name = 'all_shopping_lists.html'
    context_object_name = 'my_shopping_lists'


class ShoppingListDetails(DetailView):
    model = ShoppingLists
    template_name = "list_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_list'] = Products.objects.filter(shoppinglists=self.object.id)
        return context


class ShoppingListCreate(CreateView):
    model = ShoppingLists
    form_class = ShoppingListForm
    template_name = 'new_shopping_list.html'


def shopping_list_create(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shoppinglist = form.save()
            return redirect('details', shoppinglist.pk)
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


def product_create(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            products = form.save()
            return redirect('products')
    else:
        form = ProductsForm

    return render(request,
                  'new_product.html',
                  {'form': form})


def product_change(request, id):
    products = Products.objects.get(id=id)
    if request.method == "POST":
        form = ProductsForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductsForm(instance=products)
    return render(request,
                  'product_change.html',
                  {'products': products,
                   'form': form})


def product_delete(request, id):
    products = Products.objects.get(id=id)
    if request.method == "POST":
        products.delete()
        return redirect('products')

    return render(request,
                  'delete_conf_page_product.html',
                  {'products': products})




