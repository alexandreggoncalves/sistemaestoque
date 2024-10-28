from django.db import models
from django.urls import reverse

class Categoria(models.Model):

    # Fields
    idCategoria     = models.AutoField(primary_key=True)
    nome            = models.CharField(max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-nome']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.idCategoria)])

    def __str__(self):
        return self.nome