from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_django
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username    = request.POST.get('username')
        password    = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('dashboard')
        else:
            #eturn HttpResponse('ERRO! Usuário ou senha inválidos')
            return render(request, 'login/login.html', {'error': 'true', 'message' : 'Usuário ou senha inválidos!' })

@login_required(login_url='/sistema/login/') 
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def logout(request):
    if request.method == 'GET':
        logout_django(request)
        return redirect('dashboard')
