from django.contrib import admin
from api.models import *

admin.site.register(Vendedor)
admin.site.register(Parametro)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('codigo_cliente', 'razao_social', 'id', 'cnpj_cpf', 'status_importacao')