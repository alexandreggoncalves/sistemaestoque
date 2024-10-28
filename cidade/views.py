from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CidadeForm
from .models import Cidade

# INSERIR CIDADE
@login_required(login_url='/sistema/login/') 
def inserirCidade(request):
    if request.method == 'POST':
         form = CidadeForm(request.POST)
         if form.is_valid():
             nomeCidade = form.cleaned_data['nomeCidade']
             estado = form.cleaned_data['estado']

             cidade = Cidade.objects.create(nomeCidade=nomeCidade, estado=estado)
             cidade.save()
             form = CidadeForm()
             return render(request, 'inserirCidade.html', { 'form': form, 'message': 'Cidade inserida com sucesso!'})

    form = CidadeForm()
    return render(request, 'inserirCidade.html', { 'form': form })

# EDITAR CIDADE
@login_required(login_url='/sistema/login/') 
def editarCidade(request, id):
    if request.method == 'POST':
         Cid = Cidade.objects.filter(idCidade=id).first()
         form = CidadeForm(request.POST, instance=Cid)
         if form.is_valid():
             form.save()
             return redirect('listarCidades')
    elif request.method == 'GET':
        Cid = Cidade.objects.filter(idCidade=id).first()
        form = CidadeForm(instance=Cid)
        return render(request, 'editarCidade.html', { 'form': form })
    
# LISTAR Cidade
@login_required(login_url='/sistema/login/') 
def listarCidades(request):
    # POST PARA DELETAR Cidade
    if request.method == 'POST':
        Cidade.objects.filter(idCidade=request.POST.get('idCidade')).delete()
        return redirect('listarCidades')

    cidades = {
        'cidades': Cidade.objects.all().order_by('nomeCidade')
    }

    return render(request, 'listarCidades.html', cidades)