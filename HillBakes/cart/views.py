from django.shortcuts import render, redirect
from hb.models import Product, Cost
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import requests

# Create your views here.
#@login_required(login_url="/users/login")
def cart_add(request, productID, costID):
    cart = Cart(request)
    product = Product.objects.get(id=productID)
    cost = Cost.objects.get(id=costID)
    cart.add(product=product, cost=cost)

    url = request.GET
    
    return redirect(url["next"])


#@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("hb:home_page")


#@login_required(login_url="/users/login")
def item_increment(request, productID, costID):
    cart = Cart(request)
    product = Product.objects.get(id=productID)
    cost = Cost.objects.get(id=costID)
    cart.add(product=product, cost=cost)
    return redirect("cart:cart_detail")


#@login_required(login_url="/users/login")
def item_decrement(request, productID, costID):
    cart = Cart(request)
    product = Product.objects.get(id=productID)
    cost = Cost.objects.get(id=costID)
    cart.decrement(product=product)
    return redirect("cart:cart_detail")


#@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")


#@login_required(login_url="/users/login")
def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart/cart_detail.html', context)