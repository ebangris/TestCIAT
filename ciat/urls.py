from django.contrib import admin
from django.urls import path
from webpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mapa', views.mapa, name='mapa'),
    path('index', admin.site.urls, name='admin' ),
]



