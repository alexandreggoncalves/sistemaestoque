from django.urls import path
from . import views

urlpatterns = [
    path('registrarEntradaSaida', views.registrarEntradaSaida, name='registrarEntradaSaida'),
]