from django.urls import path
from . import views

urlpatterns = [
    path('inserirUsuario/', views.inserirUsuario, name='inserirUsuario'),
    path('listarUsuarios/', views.listarUsuarios, name='listarUsuarios'),
]