from django.urls import path
from . import views

urlpatterns = [
    path('create_client/', views.create_client_view, name='create_client'),
    path('create_product/', views.create_product_view, name='create_product'),
    path('create_order/', views.create_order_view, name='create_order'),
]