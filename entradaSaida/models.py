from django.db import models
from django.urls import reverse
from datetime import datetime
from datetime import date
from produto.models import Produto

class EntradaSaida(models.Model):
    entradaSaidaChoices = [('E', 'Entrada'), ( 'S', 'Saída')]
    # Fields
    idEntradaSaida  = models.AutoField(primary_key=True)
    descricao       = models.CharField(blank=True, null=True, max_length=50)
    idProduto       = models.ForeignKey(Produto, blank=False, null=False, on_delete=models.CASCADE)
    entradaSaida    = models.CharField(choices=entradaSaidaChoices, max_length=1, blank=False, null=False)
    quantidade      = models.IntegerField(default=0, blank=True, null=True)
    preco           = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-descricao']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.descricao)])

    def __str__(self):
        return self.descricao