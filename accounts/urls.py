from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('product/',product,name='product'),
    path('customer/<str:pk_test>/',customer,name='customer'),

    path('create_order/',createOrder,name='create_order'),
]
