from django.urls import path
from . import views

urlpatterns = [
    path('inserirFornecedor/', views.inserirFornecedor, name='inserirFornecedor'),
    path('editarFornecedor/<int:id>', views.editarFornecedor, name='editarFornecedor'),
    path('listarFornecedores/', views.listarFornecedores, name='listarFornecedores'),
]