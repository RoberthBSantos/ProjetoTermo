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
from contatos.views import listar_contatos
from contatos.views import novo_contato
from contatos.views import atualizar_contato
from contatos.views import excluir_produto
from contatos.views import nova_lista
from contatos.views import excluir_prod_lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_contatos, name = "lista_contatos"),
    path('adicionar', novo_contato, name = "adicionar_contato"),
    path('atualizar/<int:id>/', atualizar_contato, name = "atualizar_contato"),
    path('exluir/<int:id>)/', excluir_produto, name = "excluir_produto"),
    path('lista', nova_lista, name = 'adicionar_lista'),
    path('exluir_prod/<int:id>)/', excluir_prod_lista, name = "excluir_produto_lista"),
]
