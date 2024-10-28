from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nomeProduto', 'idFornecedor', 'quantidade', 'preco', 'codigoDeBarras']
        widgets = {
            'nomeProduto': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o nome do produto'}),
            'idFornecedor': forms.Select(attrs = {'class': 'form-select', 'placeholder': 'Selecione uma fornecedor'}),
            'quantidade': forms.NumberInput(attrs = {'class': 'form-control'}),
            'preco': forms.NumberInput(attrs = {'class': 'form-control'}),
            'codigoDeBarras': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o código de barras, se houver'}),
        }
        labels = {
            'idFornecedor': 'Fornecedor',
            'preco': 'Preco (0.00)',
        }