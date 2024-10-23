from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/sistema/login/') 
def inserirUsuario(request):
    if request.method == 'POST':
        

        return redirect( 'listarUsuarios' )
        
    else:
        return render(request, 'inserirUsuario.html')

@login_required(login_url='/sistema/login/') 
def listarUsuarios(request):
    User = get_user_model()
    users = User.objects.all()

    return render(request, 'listarUsuarios.html', {'users':users})