from django.db import models
from django.urls import reverse

"""
class Produto(models.Model):

    # Fields
    idProduto       = models.AutoField(primary_key=True)
    nome            = models.CharField(max_length=255)
    quantidade      = models.IntegerField(default=0)
    idFornecedor    = models.IntegerField(default=0)
    preco           = models.DecimalField(default=0)
    codigoDeBarras  = models.CharField(max_length=255)
    dataEntrada     = models.DateField(auto_now_add=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-nome']

    # Methods
    def get_absolute_url(self):
        """ """ Returns the URL to access a particular instance of the model.""" """
        return reverse('model-detail-view', args=[str(self.idProduto)])


    def __str__(self):
        return self.nome
"""