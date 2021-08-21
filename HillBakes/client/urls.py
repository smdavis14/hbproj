from django.apps import apps
from django.urls import path
from django.contrib import admin
from .views import signup, login_user, logout_user

app_name = 'client'
urlpatterns = [
  path('signup/', signup, name='signup'),
  path('login/', login_user, name='login_user'),
  path('logout/', logout_user, name='logout_user'),
]