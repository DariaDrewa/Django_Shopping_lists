from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('shopping_list/details/<int:id>', views.list_details, name='details'),
]
