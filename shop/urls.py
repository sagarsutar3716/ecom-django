from django.urls import path 

from . import views

urlpatterns = [
    path('', views.home, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"), 
    path('products/<int:myid>',views.prodview, name="productview")
]