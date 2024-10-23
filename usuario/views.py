from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
@login_required(login_url='/sistema/login/') 
def inserirUsuario(request):
    return render(request, 'inserirUsuario.html')

@login_required(login_url='/sistema/login/') 
def listarUsuarios(request):
    User = get_user_model()
    users = User.objects.all()

    return render(request, 'listarUsuarios.html', {'users':users})