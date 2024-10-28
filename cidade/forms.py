from django import forms
from .models import Cidade

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nomeCidade', 'estado']
        widgets = {
            'nomeCidade': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Informe o nome da cidade'}),
            'estado': forms.TextInput(attrs = {'class': 'form-control mb-2'})
        }