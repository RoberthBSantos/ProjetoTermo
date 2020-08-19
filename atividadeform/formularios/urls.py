"""formularios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contatos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_contatos, name = "lista_contatos"),
    path('adicionar', novo_contato, name = "adicionar_contato"),
    path('atualizar/<int:id>/', atualizar_contato, name = "atualizar_contato"),
    path('exluir/<int:id>)/', excluir_produto, name = "excluir_produto"),
    path('lista', nova_lista, name = 'adicionar_lista'),
    path('exluir_prod/<int:id>)/', excluir_prod_lista, name = "excluir_produto_lista"),
    path('gerar_documento', gerar_xlsx,name = 'gerar_documento'),
    path('novo_fornecedor', novo_fornecedor, name = 'novo_fornecedor'),
    path('listar_fornecedor', listar_fornecedor, name = 'listar_fornecedor'),
    path('gerar_docx', gerar_docx, name = 'gerar_docx'),
    path('atualizar_fornecedor/<int:id>/', atualizar_fornecedor, name = 'atualizar_fornecedor'),
    path('excluir_fornecedor/<int:id>/', excluir_fornecedor, name = 'excluir_fornecedor'),
    path('excluir_prod_lista/<int:id>',excluir_prod_lista, name = 'excluir_prod_lista'),
    path('atualizar_prod_lista/<int:id>', atualizar_prod_lista, name = 'atualizar_prod_lista'),
]
