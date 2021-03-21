from django.forms import ModelForm, DateInput, Select, TextInput, NumberInput
from django import forms

from .models import Produtos, ListaMaterial, Fornecedor, Projeto, SubItem


class FormularioContato(ModelForm):
    valor_de_compra = forms.DecimalField(max_digits=8, decimal_places=2, localize=True)

    class Meta:
        model = Produtos
        fields = ['nome', 'fabricante', 'fornecedor', 'modelo', 'unidade', 'tempo_de_instalacao', 'tempo_de_sup',
                  'grupo', 'descricao', 'valor_de_compra', 'valor_de_terceiros', 'data']
        labels = {

            'tempo_de_instalacao': 'Tempo de instalação ∆T INF.',
            'tempo_de_sup': 'Tempo de suporte ∆T SUP.',
            'descricao': 'Descricao (Que vai para o documento do termo.)',
            'data': 'Data da cotação'
        }

        widgets = {
            'data': DateInput(attrs={'type': 'date', })

        }


class FormularioSubitem(ModelForm):
    class Meta:
        model = SubItem
        fields = ['sub', 'quantidade']
        widgets = {
            'sub': Select(attrs={
                'class': 'select-com-pesquisa',
                'name': 'state',
            })
        }


class FormularioLista(ModelForm):
    class Meta:
        model = ListaMaterial
        fields = ['produto', 'quantidade']
        widgets = {'produto': Select(attrs={
            'class': 'select-com-pesquisa',
            'name': 'state'
        })}

    class Media:
        js = 'js/lista_produtos.js'


class FormularioFornecedor(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['razao_social', 'telefone', 'cnpj', 'email', 'endereco', 'numero', 'bairro', 'cidade']
        widgets = {
            'telefone': TextInput(attrs={
                'class': 'form-control',
                'minlength': '15',
                'onkeypress': '$(this).mask(\'(00) 00000-0009\')'
            }),
            'cnpj': TextInput(attrs={
                'class': 'form-control',
                'onkeypress': '$(this).mask(\'00.000.000/0000-00\')',
                'minlength': '18'
            })}


class FormularioProjeto(ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome_projeto', 'tipo_de_projeto', 'margem', 'valor_infra', 'valor_sup', 'valor_upi', 'valor_upr',
                  'valor_upe', 'convidados']


class NameForm(forms.Form):
    project_name = forms.CharField(label='Nome do Projeto', max_length=100)
