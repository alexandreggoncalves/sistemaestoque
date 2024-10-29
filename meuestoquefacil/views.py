from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required

@login_required(login_url='/sistema/login/') 
def dashboard(request):
    pathInfo = request.path
    return render(request, 'dashboard/dashboard.html', { 'pathInfo': pathInfo})

def logout(request):
    if request.method == 'GET':
        logout_django(request)
        return redirect('dashboard')