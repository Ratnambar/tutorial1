# from django.contrib import admin
from django.urls import path
from .views import product_list, product_detail, health_check

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('health/', health_check, name='health_check'),
]