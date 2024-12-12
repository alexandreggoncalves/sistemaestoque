from django import forms
from .models import RequisicaoCompra


class RequisicaoForm(forms.ModelForm):

    class Meta:
        valores = [
            ('0', 'Aguardando'),
            ('1',"Aprovado"),
            ('2',"Reprovado")
        ] 

        required_css_class = 'required'
        model = RequisicaoCompra       
        fields = ['nomeProduto', 'idCategoria', 'idFornecedor', 'codigoDeBarras', 'status', 'observacao']        
        widgets = {
            'nomeProduto': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o nome do produto'}),
            'idCategoria': forms.Select(attrs = {'class': 'form-select', 'placeholder': 'Selecione uma categoria'}),
            'idFornecedor': forms.Select(attrs = {'class': 'form-select', 'placeholder': 'Selecione um fornecedor'}),
            'observacao': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Informe uma observação, caso deseje'}),
            'codigoDeBarras': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o código de barras'}),
            'status': forms.Select(choices=valores, attrs = {'class': 'form-control'}), 
        }
        labels = {
            'nomeProduto': 'Nome do Produto', 
            'idCategoria': 'Categoria',
            'idFornecedor': 'Fornecedor',
            'status': 'Status Requisição',
        }

    def __init__(self, *args, **kwargs):
        super(RequisicaoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'