from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('shopping_list/', views.ShoppingListView.as_view(), name='shopping_list'),
    path('shopping_list/details/<int:pk>', views.ShoppingListDetails.as_view(), name='details'),
]
