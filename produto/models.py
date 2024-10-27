from django.db import models
from django.urls import reverse

class Produto(models.Model):

    # Fields
    idProduto       = models.AutoField(primary_key=True)
    idCategoria     = models.IntegerField(default=0)
    nome            = models.CharField(max_length=255)
    quantidade      = models.IntegerField(default=0)
    idFornecedor    = models.IntegerField(default=0)
    preco           = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    codigoDeBarras  = models.CharField(max_length=255)
    dataEntrada     = models.DateField(auto_now_add=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-nome']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.idProduto)])


    def __str__(self):
        return self.nome