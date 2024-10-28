from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nomeCategoria']
        widgets = {
            'nomeCategoria': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o nome da categoria'})
        }