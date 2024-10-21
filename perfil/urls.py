from django.urls import path
from . import views

urlpatterns = [
    path('inserirPerfil/', views.inserirPerfil, name='inserirPerfil'),
]