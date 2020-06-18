from django.contrib import admin
from .models import Produtos, ListaMaterial, Fornecedor, Grupos

admin.site.register(Produtos)
admin.site.register(ListaMaterial)
admin.site.register(Fornecedor)
admin.site.register(Grupos)