from django.contrib import admin
from . models import Area


class arealAdmin(admin.ModelAdmin):
    list_display = ( 'idArea', 'nome', 'idAreaPai' )

admin.site.register(Area, arealAdmin)