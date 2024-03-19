from django.urls import path
from .views import ProductsListView, ShoppingListView, ShoppingListDetails, Main

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('shopping_list/', ShoppingListView.as_view(), name='shopping_list'),
    path('<int:pk>', ShoppingListDetails.as_view(), name='details'),
]
