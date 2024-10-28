from django.db import models
from django.urls import reverse

class Cidade(models.Model):

    # Fields
    idCidade        = models.AutoField(primary_key=True)
    nomeCidade      = models.CharField(max_length=255)
    estado          = models.CharField(max_length=2)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-nomeCidade']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.idCidade)])

    def __str__(self):
        return self.nomeCidade