from django.urls import path
from .views import ordered_products

urlpatterns = [
    path('ordered_products/', ordered_products, name='ordered_products'),
]