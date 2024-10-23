from django.urls import path
from . import views

urlpatterns = [
    path('inserirProduto/', views.inserirProduto, name='inserirProduto'),
    path('listarProdutos/', views.listarProdutos, name='listarProdutos'),
]