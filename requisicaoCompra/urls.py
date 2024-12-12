from django.urls import path
from . import views

urlpatterns = [
    path('inserirRequisicao/', views.inserirRequisicao, name='inserirRequisicao'),
    path('editarRequisicao/<int:id>', views.editarRequisicao, name='editarRequisicao'),
    path('listarRequisicoes/', views.listarRequisicoes, name='listarRequisicoes'),
]