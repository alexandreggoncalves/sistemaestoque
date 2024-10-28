from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import CategoriaForm
from .models import Categoria

# INSERIR CATEGORIA
@login_required(login_url='/sistema/login/') 
def inserirCategoria(request):
    if request.method == 'POST':
         form = CategoriaForm(request.POST)
         if form.is_valid():
             nomeCategoria = form.cleaned_data['nomeCategoria']

             categoria = Categoria.objects.create(nomeCategoria=nomeCategoria)
             categoria.save()
             form = CategoriaForm()
             return render(request, 'inserirCategoria.html', { 'form': form, 'message': 'Categoria inserida com sucesso!'})

    form = CategoriaForm()
    return render(request, 'inserirCategoria.html', { 'form': form})

# EDITAR CATEGORIA
@login_required(login_url='/sistema/login/') 
def editarCategoria(request, id):
    if request.method == 'POST':
         Cat = Categoria.objects.filter(idCategoria=id).first()
         form = CategoriaForm(request.POST, instance=Cat)
         if form.is_valid():
             #nome = form.cleaned_data['nome']
             #categoria = Categoria.objects.update(nome=nome)
             form.save()
             return redirect('listarCategorias')
    elif request.method == 'GET':
        Cat = Categoria.objects.filter(idCategoria=id).first()
        form = CategoriaForm(instance=Cat)
        return render(request, 'editarCategoria.html', { 'form': form})
    
# LISTAR CATEGORIA
@login_required(login_url='/sistema/login/') 
def listarCategorias(request):
    # POST PARA DELETAR CATEGORIA
    if request.method == 'POST':
        Categoria.objects.filter(idCategoria=request.POST.get('idCategoria')).delete()
        return redirect('listarCategorias')
    
    busca = request.GET.get('busca')

    if busca:
        categorias = Categoria.objects.filter(nomeCategoria__icontains=busca).order_by('nomeCategoria')
    else:
        categorias = Categoria.objects.all().order_by('nomeCategoria')

    categoria_paginator = Paginator(categorias, 10)
    page_num = request.GET.get('page')
    page = categoria_paginator.get_page(page_num)

    return render(request, 'listarCategorias.html', { 'page': page })