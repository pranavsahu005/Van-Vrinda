from django.urls import path
from .views import *
producturls=[
    path('addproduct',addProduct,name='addProduct')
]