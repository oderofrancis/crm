from django.urls import path
from .views import *

urlpatterns = [

    path('register/',registerPage,name='register'),
    path('login/',loginPage,name='login'),

    path('',dashboard,name='dashboard'),
    path('product/',product,name='product'),
    path('customer/<str:pk_test>/',customer,name='customer'),

    path('create_order/<str:pk>/',createOrder,name='create_order'),
    path('update_order/<str:pk>/',updateOrder,name='update_order'),
    path('delete_order/<str:pk>/',deleteOrder,name='delete_order'),
]
