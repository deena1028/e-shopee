from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('',views.index),
    path('update_cart_item',views.updateCartitem),
    path('login',views.login),
    path('login_user',views.login_user),
    path('home',views.index),
    path('cart',views.viewcart),
    path('delete_cart',views.delete_cart),
    path('checkout',views.checkout),
    path('logout',views.logout),
    path('shop',views.shop),
    path('search',views.search),
    path('search_category/<id>',views.search_category),
]

