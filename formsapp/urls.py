from django.urls import path
from . import views

app_name = 'formsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.Client, name='client'),
    path('client/<int:client_id>/', views.client_order, name='client_order'),

]