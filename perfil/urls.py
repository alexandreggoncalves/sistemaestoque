from django.urls import path
from . import views

urlpatterns = [
    path('novoPerfil/', views.novoPerfil, name='novoPerfil'),
]