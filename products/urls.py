from django.urls import path
from .views import (
    ProductsListView, ShoppingListView, ShoppingListDetails, Main, ShoppingListCreate,
    shopping_list_change, shopping_list_delete,product_create, product_change, product_delete
)

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('shopping_list/', ShoppingListView.as_view(), name='shopping_list'),
    path('<int:pk>', ShoppingListDetails.as_view(), name='details'),
    path('shopping_list/add/', ShoppingListCreate.as_view(), name='create'),
    path('shopping_list/<int:id>/change/', shopping_list_change, name='change'),
    path('shopping_list/<int:id>/delete/', shopping_list_delete, name='delete'),
    path('products/add/', product_create, name='product_create'),
    path('products/<int:id>/change/', product_change, name='product_change'),
    path('products/<int:id>/delete/', product_delete, name='product_delete')
]
