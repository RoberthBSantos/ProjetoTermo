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
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_contatos', listar_contatos, name = "lista_contatos"),
    path('',listar_projetos, name= 'lista_projetos'),
    path('novo_projeto', novo_projeto, name= 'novo_projeto'),
    path('adicionar', novo_contato, name = "adicionar_contato"),
    path('atualizar_projeto/<int:id>', atualizar_projeto, name = 'atualizar_projeto'),
    path('atualizar/<int:id>/', atualizar_contato, name = "atualizar_contato"),
    path('exluir/<int:id>)/', excluir_produto, name = "excluir_produto"),
    path('lista/<int:id>', nova_lista, name = 'lista/id/'),
    path('exluir_prod/<int:id>)/', excluir_prod_lista, name = "excluir_produto_lista"),
    path('gerar_documento/<int:id>/', gerar_xlsx,name = 'gerar_documento'),
    path('novo_fornecedor', novo_fornecedor, name = 'novo_fornecedor'),
    path('listar_fornecedor', listar_fornecedor, name = 'listar_fornecedor'),
    path('gerar_docx/<int:id>/', gerar_docx, name = 'gerar_docx'),
    path('atualizar_fornecedor/<int:id>/', atualizar_fornecedor, name = 'atualizar_fornecedor'),
    path('excluir_fornecedor/<int:id>/', excluir_fornecedor, name = 'excluir_fornecedor'),
    path('excluir_prod_lista/<int:id>',excluir_prod_lista, name = 'excluir_prod_lista'),
    path('atualizar_prod_lista/<int:id>', atualizar_prod_lista, name = 'atualizar_prod_lista'),
    path('excluir_lista_produto/<int:id>',excluir_lista_produto, name = 'excluir_lista_produto'),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('listar_downloads',listar_download, name = 'listar_downloads'),
    path('formulario_docs/<int:id>',get_name_docx, name = 'formulario_docs'),
    path('formulario_xlsx/<int:id>',get_name_xlsx,name = 'formulario_xlsx'),
    path('delete_doc/<int:id>', delete_doc, name = 'delete_doc'),
    path('limpar_lista',limpar_lista, name = 'limpar_lista'),
    path('deletar_projeto/<int:id>',deletar_projeto, name = 'deletar_projeto'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)