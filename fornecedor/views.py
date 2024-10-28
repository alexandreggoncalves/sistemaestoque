from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import FornecedorForm
from .models import Fornecedor

# INSERIR FORNECEDOR
@login_required(login_url='/sistema/login/') 
def inserirFornecedor(request):
    if request.method == 'POST':
         form = FornecedorForm(request.POST)
         if form.is_valid():
             nomeFornecedor       = form.cleaned_data['nomeFornecedor']
             idCidade   = form.cleaned_data['idCidade']

             fornecedor = Fornecedor.objects.create(nomeFornecedor=nomeFornecedor, idCidade=idCidade)
             fornecedor.save()
             form = FornecedorForm()
             return render(request, 'inserirFornecedor.html', { 'form': form, 'message': 'Fornecedor inserido com sucesso!'})

    form = FornecedorForm()
    return render(request, 'inserirFornecedor.html', { 'form': form })

# EDITAR FORNECEDOR
@login_required(login_url='/sistema/login/') 
def editarFornecedor(request, id):
    if request.method == 'POST':
         Forn = Fornecedor.objects.filter(idFornecedor=id).first()
         form = FornecedorForm(request.POST, instance=Forn)
         if form.is_valid():
             form.save()
             return redirect('listarFornecedores')
    elif request.method == 'GET':
        Forn = Fornecedor.objects.filter(idFornecedor=id).first()
        form = FornecedorForm(instance=Forn)
        return render(request, 'editarFornecedor.html', { 'form': form })
    
# LISTAR FORNECEDOR
@login_required(login_url='/sistema/login/') 
def listarFornecedores(request):
    # POST PARA DELETAR FORNECEDOR
    if request.method == 'POST':
        Fornecedor.objects.filter(idFornecedor=request.POST.get('idFornecedor')).delete()
        return redirect('listarFornecedores')

    fornecedores = {
        'fornecedores': Fornecedor.objects.all().order_by('nomeFornecedor')
    }

    return render(request, 'listarFornecedores.html', fornecedores)