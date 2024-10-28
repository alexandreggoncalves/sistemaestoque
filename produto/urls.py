from django.urls import path
from . import views

urlpatterns = [
    path('inserirProduto/', views.inserirProduto, name='inserirProduto'),
    path('editarProduto/<int:id>', views.editarProduto, name='editarProduto'),
    path('listarProdutos/', views.listarProdutos, name='listarProdutos'),
]