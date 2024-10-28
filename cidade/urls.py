from django.urls import path
from . import views

urlpatterns = [
    path('inserirCidade/', views.inserirCidade, name='inserirCidade'),
    path('editarCidade/<int:id>', views.editarCidade, name='editarCidade'),
    path('listarCidades/', views.listarCidades, name='listarCidades'),
]