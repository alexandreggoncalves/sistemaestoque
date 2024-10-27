from django.urls import path
from . import views

urlpatterns = [
    path('inserirCategoria/', views.inserirCategoria, name='inserirCategoria'),
    path('editarCategoria/<int:id>', views.editarCategoria, name='editarCategoria'),
    path('listarCategorias/', views.listarCategorias, name='listarCategorias'),
]