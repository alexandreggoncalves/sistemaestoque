from django import forms
from .models import EntradaSaida

CHOICES = (('E', 'Entrada',), ('S', 'Saída',))

class EntradaSaidaForm(forms.ModelForm):    
    class Meta:
        model = EntradaSaida
        fields = ['entradaSaida', 'idProduto' ]
        widgets = {
            
        }
        labels = {
            'entradaSaida': 'Entrada / Saída',
            'idProduto': 'Produto',
        }