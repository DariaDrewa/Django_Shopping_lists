from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Products, ShoppingLists


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_list'] = Products.objects.filter(shoppinglists=self.object.id)
        return context


class Main(generic.ListView):
    template_name = 'main.html'

    def get_queryset(self):
        qs1 = Products.objects.all()
        qs2 = ShoppingLists.objects.all()