from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import RequisicaoForm
from .models import RequisicaoCompra

# INSERIR PRODUTO
@login_required(login_url='/sistema/login/') 
def inserirRequisicao(request):
    if request.method == 'POST':
         form = RequisicaoForm(request.POST)
         if form.is_valid():
             nomeProduto    = form.cleaned_data['nomeProduto']
             idCategoria    = form.cleaned_data['idCategoria']
             idFornecedor   = form.cleaned_data['idFornecedor']
             codigoDeBarras = form.cleaned_data['codigoDeBarras']
             observacao     = form.cleaned_data['observacao']

             requisicaoCompra = RequisicaoCompra.objects.create(nomeProduto=nomeProduto, 
                                                                idFornecedor=idFornecedor, 
                                                                idCategoria=idCategoria, 
                                                                codigoDeBarras=codigoDeBarras, 
                                                                observacao=observacao)
             requisicaoCompra.save()
             form = RequisicaoForm()

             return render(request, 'inserirRequisicao.html', { 'form': form, 'message': 'Requisição inserida com sucesso!'})

    form = RequisicaoForm()
    return render(request, 'inserirRequisicao.html', { 'form': form })

# EDITAR FORNECEDOR
@login_required(login_url='/sistema/login/') 
def editarRequisicao(request, id):
    if request.method == 'POST':
         Prod = RequisicaoCompra.objects.filter(idRequisicao=id).first()
         form = RequisicaoForm(request.POST, instance=Prod)
         if form.is_valid():
             form.save()
             return redirect('listarRequisicoes')
    elif request.method == 'GET':
        Prod = RequisicaoCompra.objects.filter(idRequisicao=id).first()
        form = RequisicaoForm(instance=Prod)
        return render(request, 'editarRequisicao.html', { 'form': form })

# LISTAR PRODUTOS
@login_required(login_url='/sistema/login/') 
def listarRequisicoes(request):
    # POST PARA DELETAR PRODUTO
    if request.method == 'POST':
        RequisicaoCompra.objects.filter(idProduto=request.POST.get('idProduto')).delete()
        return redirect('listarRequisicoes')

    busca = request.GET.get('busca')

    if busca:
        requisicoes = RequisicaoCompra.objects.filter(nomeProduto__icontains=busca).order_by('nomeProduto')
    else:
        requisicoes = RequisicaoCompra.objects.all().order_by('nomeProduto')

    requisicao_paginator = Paginator(requisicoes, 10)
    page_num = request.GET.get('page')
    page = requisicao_paginator.get_page(page_num)
    return render(request, 'listarRequisicoes.html', {'page': page})