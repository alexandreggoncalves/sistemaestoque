from django.db import models
from django.urls import reverse
from cidade.models import Cidade

class Fornecedor(models.Model):

    # Fields
    idFornecedor    = models.AutoField(primary_key=True)
    nomeFornecedor  = models.CharField(max_length=255)
    idCidade        = models.ForeignKey(Cidade, blank=True, null=True, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-nomeFornecedor']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.idFornecedor)])

    def __str__(self):
        return self.nomeFornecedor