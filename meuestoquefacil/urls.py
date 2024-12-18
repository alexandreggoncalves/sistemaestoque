"""
URL configuration for meuestoquefacil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authuser/', include('authuser.urls')),
    path('usuario/', include('usuario.urls')),
    path('produto/', include('produto.urls')),
    path('categoria/', include('categoria.urls')),
    path('cidade/', include('cidade.urls')),
    path('fornecedor/', include('fornecedor.urls')),
    path('entradaSaida/', include('entradaSaida.urls')),
    path('requisicaoCompra/', include('requisicaoCompra.urls')),
    path('relatorio/', include('relatorio.urls')),
    path('sistema/', include('sistema.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]