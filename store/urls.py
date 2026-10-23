from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('buy-now/<int:pk>/', views.buy_now, name='buy_now'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
]