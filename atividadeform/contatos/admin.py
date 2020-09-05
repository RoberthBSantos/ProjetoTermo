from django.contrib import admin
from .models import Produtos, ListaMaterial, Fornecedor, Grupos, Projeto, DocFiles

admin.site.register(Produtos)
admin.site.register(ListaMaterial)
admin.site.register(Fornecedor)
admin.site.register(Grupos)
admin.site.register(Projeto)
admin.site.register(DocFiles)