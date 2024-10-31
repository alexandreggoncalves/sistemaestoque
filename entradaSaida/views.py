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
    if request.method == 'POST':
        idProduto       = request.POST.get('idProdutoES')
        entradaSaida    = request.POST.get('entradaSaida')
        quantidade      = request.POST.get('quantidade')
        preco           = request.POST.get('preco')

        data = { 'idProduto': idProduto,
                    'entradaSaida': entradaSaida, 
                    'quantidade': quantidade, 
                    'preco': preco,
                }
    
        produto = Produto.objects.get(idProduto=request.POST.get('idProdutoES'))

        # faz um novo check na quantidade para prevenir erros
        if entradaSaida == 'E':
            quantidadeProduto = int(produto.quantidade) + int(quantidade)
            flagSalvar = True
        elif entradaSaida == 'S':
            if int(produto.quantidade) >= int(quantidade):
                quantidadeProduto = int(produto.quantidade) - int(quantidade)
                flagSalvar = True
            else:
                flagSalvar = False

        if flagSalvar == True:
            # salvando o form de entrada e saida
            form = EntradaSaida.objects.create(idProduto=produto, 
                                                descricao='',
                                                entradaSaida=entradaSaida, 
                                                quantidade=quantidade, 
                                                preco=preco)
            form.save()

            # update na quantidade de produto
            produto.quantidade = quantidadeProduto
            produto.save()

        return JsonResponse(data)
    else:
        # realiza a busca na tabela de produtos
        produtos = Produto.objects.filter(nomeProduto__icontains=request.GET.get('txtBusca'), codigoDeBarras__icontains=request.GET.get('txtBarras')).order_by('nomeProduto')
        
        # cria um dicionáiro para o retorno da busca e aciona o resultado.
        dataReturn = {}
        if produtos:
            for produtos in produtos: # adicona os resultados no dicionario
                dataReturn[produtos.idProduto] = {'nome': produtos.nomeProduto, 
                                                'quantidade': produtos.quantidade}
        else:
            dataReturn[0] = {'nome': 'não formam encontrados produtos',
                             'quantidade': '0'}
            
        # retorna os dados via Json
        return JsonResponse(dataReturn)