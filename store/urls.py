
from django.contrib import admin
from django.urls import path
from .views import index,sign_up,product

urlpatterns = [
path('',index),
path('signup/',sign_up),
path('product/',product)

]
