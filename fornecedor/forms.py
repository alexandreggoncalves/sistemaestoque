from django import forms
from .models import Fornecedor
#from cidade.models import Cidade

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nomeFornecedor', 'idCidade']
        widgets = {
            'nomeFornecedor': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o nome do fornecedor'}),
            'idCidade': forms.Select(attrs = {'class': 'form-select', 'placeholder': 'Selecione uma cidade'}),
        }
        labels = {
            'idCidade': 'Cidade'
        }