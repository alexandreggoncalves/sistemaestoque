from django.contrib import admin
from . models import Perfil


class perfilAdmin(admin.ModelAdmin):
    list_display = ( 'idPerfil', 'nome', 'areasDeAcesso' )

admin.site.register(Perfil, perfilAdmin)