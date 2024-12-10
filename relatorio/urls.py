from django.urls import path
from . import views

urlpatterns = [
    path('entradaSaida/', views.entradaSaida, name='entradaSaida'),
    path('balanco/', views.balanco, name='balanco'),
]