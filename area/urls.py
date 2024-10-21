from django.urls import path
from . import views

urlpatterns = [
    path('inserirArea/', views.inserirArea, name='inserirArea'),
]