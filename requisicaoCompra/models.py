from django.db import models
from django.urls import reverse
from datetime import datetime
from datetime import date
from categoria.models import Categoria
from fornecedor.models import Fornecedor

class RequisicaoCompra(models.Model):

    # Fields
    idRequisicao    = models.AutoField(primary_key=True)
    idCategoria     = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.CASCADE)
    idFornecedor    = models.ForeignKey(Fornecedor, blank=False, null=False, on_delete=models.CASCADE)
    nomeProduto     = models.CharField(max_length=255, blank=False, null=False)
    quantidade      = models.IntegerField(default=0, blank=True, null=True)
    observacao      = models.TextField(blank=True, null=True)
    codigoDeBarras  = models.CharField(max_length=255, blank=True, null=True)
    dataSolicitacao = models.DateField(auto_now_add=True)
    status          = models.IntegerField(default=0, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-nomeProduto']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.idRequisicao)])

    def __str__(self):
        return self.nomeProduto
