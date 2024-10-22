from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/sistema/login/') 
def inserirUsuario(request):
    return render(request, 'inserirUsuario.html')

@login_required(login_url='/sistema/login/') 
def listarUsuarios(request):
    return render(request, 'listarUsuarios.html')