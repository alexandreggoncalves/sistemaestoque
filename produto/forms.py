from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nomeProduto', 'idCategoria', 'idFornecedor', 'quantidade', 'preco', 'codigoDeBarras']
        widgets = {
            'nomeProduto': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o nome do produto'}),
            'idCategoria': forms.Select(attrs = {'class': 'form-select', 'placeholder': 'Selecione uma categoria'}),
            'idFornecedor': forms.Select(attrs = {'class': 'form-select', 'placeholder': 'Selecione um fornecedor'}),
            'quantidade': forms.NumberInput(attrs = {'class': 'form-control'}),
            'preco': forms.NumberInput(attrs = {'class': 'form-control'}),
            'codigoDeBarras': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o código de barras, se houver'}),
        }
        labels = {
            'idCategoria': 'Categoria',
            'idFornecedor': 'Fornecedor',
            'preco': 'Preco (0.00)',
        }