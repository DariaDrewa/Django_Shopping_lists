from django.urls import path
from .views import ProductsListView, ShoppingListView, ShoppingListDetails, Main, shopping_list_create

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('shopping_list/', ShoppingListView.as_view(), name='shopping_list'),
    path('<int:pk>', ShoppingListDetails.as_view(), name='details'),
    path('shopping_list/add/', shopping_list_create, name='shopping_list_create')
]
