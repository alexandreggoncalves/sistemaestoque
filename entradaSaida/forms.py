from django import forms
from .models import EntradaSaida

CHOICES = (('E', 'Entrada',), ('S', 'Saída',))

class EntradaSaidaForm(forms.ModelForm):    
    class Meta:
        model = EntradaSaida
        fields = ['entradaSaida', 'quantidade', 'preco', ]
        widgets = {
            'entradaSaida': forms.Select(choices=CHOICES, attrs = {'class': 'form-control form-control-sm', 'width': '100'}), 
            'quantidade': forms.TextInput(attrs = {'class': 'form-control'}),  
            'preco': forms.TextInput(attrs = {'class': 'form-control'}),      
        }
        labels = {
            'entradaSaida': 'Entrada / Saída',
        }