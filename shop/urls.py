from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<int:item_id>/', views.increase_cart, name='increase'),
    path('decrease/<int:item_id>/', views.decrease_cart, name='decrease'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('check-coupon/',views.check_coupon,name='check_coupon'),
]
