from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    dataValidade = forms.DateField(
        label = 'Data de Validade', 
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date', 
            }),
            input_formats=('%Y-%m-%d',),
        )

    class Meta:
        required_css_class = 'required'
        model = Produto       
        fields = ['nomeProduto', 'idCategoria', 'idFornecedor', 'dataValidade', 'preco', 'codigoDeBarras', 'descricao']        
        widgets = {
            'nomeProduto': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o nome do produto'}),
            'idCategoria': forms.Select(attrs = {'class': 'form-select', 'placeholder': 'Selecione uma categoria'}),
            'idFornecedor': forms.Select(attrs = {'class': 'form-select', 'placeholder': 'Selecione um fornecedor'}),
            'preco': forms.NumberInput(attrs = {'class': 'form-control'}),
            'descricao': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Informe a descrição do produto'}),
            'codigoDeBarras': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o código de barras'}),
        }
        labels = {
            'idCategoria': 'Categoria',
            'idFornecedor': 'Fornecedor',
            'preco': 'Preco (0.00)',
        }

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'