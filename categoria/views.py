from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CategoriaForm
from .models import Categoria

# INSERIR CATEGORIA
@login_required(login_url='/sistema/login/') 
def inserirCategoria(request):
    if request.method == 'POST':
         form = CategoriaForm(request.POST)
         if form.is_valid():
             nome = form.cleaned_data['nome']

             categoria = Categoria.objects.create(nome=nome)
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
    categorias = {
        'categorias': Categoria.objects.all().order_by('nome')
    }

    return render(request, 'listarCategorias.html', categorias)