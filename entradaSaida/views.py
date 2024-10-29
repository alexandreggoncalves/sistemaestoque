from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import EntradaSaidaForm
from .models import EntradaSaida

# INSERIR ENTRADA/SAIDA
@login_required(login_url='/sistema/login/') 
def registrarEntradaSaida(request):
    
    form = EntradaSaidaForm()
    return render(request, 'registrarEntradaSaida.html', { 'form': form})