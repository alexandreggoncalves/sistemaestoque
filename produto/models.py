from django.db import models
from django.urls import reverse
from datetime import datetime
from categoria.models import Categoria
from fornecedor.models import Fornecedor

class Produto(models.Model):

    # Fields
    idProduto       = models.AutoField(primary_key=True)
    idCategoria     = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    idFornecedor    = models.ForeignKey(Fornecedor, blank=True, null=True, on_delete=models.CASCADE)
    nomeProduto     = models.CharField(max_length=255)
    quantidade      = models.IntegerField(default=0)
    preco           = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    dataVencimento  = models.DateField(blank=True, null=True)
    descricao       = models.TextField(blank=True, null=True)
    codigoDeBarras  = models.CharField(max_length=255)
    dataEntrada     = models.DateField(auto_now_add=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-nomeProduto']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.idProduto)])

    def __str__(self):
        return self.nomeProduto