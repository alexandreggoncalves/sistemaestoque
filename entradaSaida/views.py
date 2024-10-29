from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .forms import EntradaSaidaForm
from .models import EntradaSaida
from produto.models import Produto

# INSERIR ENTRADA/SAIDA
@login_required(login_url='/sistema/login/') 
def registrarEntradaSaida(request):
    
    form = EntradaSaidaForm()
    return render(request, 'registrarEntradaSaida.html', { 'form': form})

# BUSCA DE PRODUTOS
@login_required(login_url='/sistema/login/') 
def buscarProdutos(request):

    # realiza a busca na tabela de produtos
    produtos = Produto.objects.filter(nomeProduto__icontains=request.GET.get('txtBusca')).order_by('nomeProduto')
    
    # cria um dicionáiro para o retorno da busca e aciona o resultado.
    dataReturn = {}
    for produtos in produtos: # adicona os resultados no dicionario
        dataReturn[produtos.idProduto] = produtos.nomeProduto

    # retorna os dados via Json
    return JsonResponse(dataReturn)