from django.shortcuts import render, reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def signup(request):
    print('METHOD', request.method)
    if request.method == 'GET':
        return render(request, 'client/login.html')
    elif request.method == 'POST':
        # get data from form
        form = request.POST
        username = form['username']
        password = form['password']
        first_name = form['first_name']
        last_name = form['last_name']
        email = form['email']

        # create user. username, email, password order matters
        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)

        login(request, user)

        return HttpResponseRedirect(reverse('hb:home_page'))


def login_user(request):
    # user visits page
    if request.method == 'GET':
        return render(request, 'client/login.html')
    # user submits form
    elif request.method == 'POST':
        # get form data
        form = request.POST
        username = form['username']
        password = form['password']

        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)

        return HttpResponseRedirect(reverse('hb:home_page'))


def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('hb:home_page'))