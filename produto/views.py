from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ProdutoForm
from .models import Produto

# INSERIR PRODUTO
@login_required(login_url='/sistema/login/') 
def inserirProduto(request):
    if request.method == 'POST':
         form = ProdutoForm(request.POST)
         if form.is_valid():
             nomeProduto    = form.cleaned_data['nomeProduto']
             idCategoria    = form.cleaned_data['idCategoria']
             idFornecedor   = form.cleaned_data['idFornecedor']
             dataVencimento = form.cleaned_data['dataVencimento']
             preco          = form.cleaned_data['preco']
             codigoDeBarras = form.cleaned_data['codigoDeBarras']

             produto = Produto.objects.create(nomeProduto=nomeProduto, idFornecedor=idFornecedor, idCategoria=idCategoria, dataVencimento=dataVencimento, preco=preco, codigoDeBarras=codigoDeBarras)
             produto.save()
             form = ProdutoForm()
             return render(request, 'inserirProduto.html', { 'form': form, 'message': 'Produto inserido com sucesso!'})

    form = ProdutoForm()
    return render(request, 'inserirProduto.html', { 'form': form })

# EDITAR FORNECEDOR
@login_required(login_url='/sistema/login/') 
def editarProduto(request, id):
    if request.method == 'POST':
         Prod = Produto.objects.filter(idProduto=id).first()
         form = ProdutoForm(request.POST, instance=Prod)
         if form.is_valid():
             form.save()
             return redirect('listarProdutos')
    elif request.method == 'GET':
        Prod = Produto.objects.filter(idProduto=id).first()
        form = ProdutoForm(instance=Prod)
        return render(request, 'editarProduto.html', { 'form': form })

# LISTAR PRODUTOS
@login_required(login_url='/sistema/login/') 
def listarProdutos(request):
    # POST PARA DELETAR PRODUTO
    if request.method == 'POST':
        Produto.objects.filter(idProduto=request.POST.get('idProduto')).delete()
        return redirect('listarProdutos')

    busca = request.GET.get('busca')

    if busca:
        produtos = Produto.objects.filter(nomeProduto__icontains=busca).order_by('nomeProduto')
    else:
        produtos = Produto.objects.all().order_by('nomeProduto')

    produto_paginator = Paginator(produtos, 10)
    page_num = request.GET.get('page')
    page = produto_paginator.get_page(page_num)

    return render(request, 'listarProdutos.html', {'page': page})