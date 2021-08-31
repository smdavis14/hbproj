from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('cart/add/<int:productID>/<int:costID>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:productID>/<int:costID>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:productID>/<int:costID>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]