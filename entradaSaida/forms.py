from django import forms
from .models import EntradaSaida

CHOICES = (('E', 'Entrada',), ('S', 'Saída',))

class EntradaSaidaForm(forms.ModelForm):    
    class Meta:
        model = EntradaSaida
        fields = ['entradaSaida', 'quantidade', 'preco', ]
        widgets = {
            'entradaSaida': forms.Select(attrs = {'class': 'form-control'}), 
            'quantidade': forms.TextInput(attrs = {'class': 'form-control'}),  
            'preco': forms.TextInput(attrs = {'class': 'form-control'}),      
        }
        labels = {
            'entradaSaida': 'Entrada / Saída',
        }