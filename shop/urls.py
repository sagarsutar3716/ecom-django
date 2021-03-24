from django.urls import path 

from . import views

urlpatterns = [
    path('', views.home, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('history/', views.myorders, name="myorders"), 
    path('products/<int:myid>',views.prodview, name="productview"),
    path('product_api/', views.product_api, name="product_api")

]