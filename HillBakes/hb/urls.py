from django.apps import apps
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page, cookies, cakes, cake_balls, about

app_name = 'hb'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('cookies/', cookies, name='cookies'),
    path('cakes/', cakes, name='cakes'),
    path('cake_balls/', cake_balls, name='cake_balls'),
    path('about/', about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)