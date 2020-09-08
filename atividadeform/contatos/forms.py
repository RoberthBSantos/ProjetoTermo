from django.forms import ModelForm, DateInput
from django import forms
from phone_field import PhoneNumber
from .models import Produtos, ListaMaterial, Fornecedor, Projeto

class FormularioContato(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome','fabricante','fornecedor','modelo','grupo','descricao','valor','data']
        widgets = {
            'data': DateInput(attrs={'type': 'date',})
        }

class FormularioLista(ModelForm):
    class Meta:
        model = ListaMaterial
        fields = ['produto','quantidade']

class FormularioFornecedor(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['razao_social','telefone']

class FormularioProjeto(ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome_projeto','itens_lista']

class NameForm(forms.Form):
    project_name = forms.CharField(label='Nome do Projeto', max_length=100)