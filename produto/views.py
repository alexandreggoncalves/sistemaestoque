from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/sistema/login/') 
def inserirProduto(request):
    return render(request, 'inserirProduto.html')

@login_required(login_url='/sistema/login/') 
def listarProdutos(request):
    Prod        = Produto()
    objProduto  = Prod.objects.all()

    return render(request, 'listarUsuarios.html', {'objProduto':objProduto})