
from django.contrib import admin
from django.urls import path
from .views import index,sign_up,product,Log_in,log_out,cart, checkout,order_view,home
from .middlewares.auth import auth_middleware

urlpatterns = [
path('',index),
path('signup/',sign_up),
path('product/',product,name="product"),
path('home/',home,name='home'),
path('login/',Log_in.as_view(),name="login"),
path('logout/',log_out,name="logout"),
path('cart/',auth_middleware(cart),name="cart"),
path('checkout/',checkout,name="checkout"),
path('order_view/', auth_middleware(order_view.as_view()), name="order")


]
