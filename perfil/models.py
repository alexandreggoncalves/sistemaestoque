from django.db import models
from django.urls import reverse

class Perfil(models.Model):

    # Fields
    idPerfil        = models.AutoField(primary_key=True)
    nome            = models.CharField(max_length=100)
    areasDeAcesso   = models.TextField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-nome']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.idPerfil)])


    def __str__(self):
        return self.nome