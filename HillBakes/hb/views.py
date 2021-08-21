from django.shortcuts import render, reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Category, Product
# from django.contrib.auth import authenticate


def home_page(request):
    return render(request, 'hb/index.html')


def cookies(request):
    cookie = Product.objects.filter(category=1)
    price = cookie[0].costField.all()
    context = {
        'cookie': cookie,
        'price': price,
    }

    return render(request, 'hb/cookies.html', context)


def cakes(request):
    cake = Product.objects.filter(category=2)
    price = cake[0].costField.all()
    context = {
        'cake': cake,
        'price': price,
    }
    return render(request, 'hb/cakes.html', context)


def cake_balls(request):
    cake_ball = Product.objects.filter(category=3)
    price = cake_ball[0].costField.all()
    context = {
        'cake_ball': cake_ball,
        'price': price,
    }
    return render(request, 'hb/cake_balls.html', context)


def about(request):
    return render(request, 'hb/about.html')
