from django.forms import ModelForm, DateInput
from django import forms
from .models import Produtos, ListaMaterial, Fornecedor, Projeto


class FormularioContato(ModelForm):
    valor_de_compra = forms.DecimalField(max_digits=8, decimal_places=2, localize=True)
    class Meta:
        model = Produtos
        fields = ['nome','fabricante','fornecedor','modelo','unidade','tempo_de_instalacao','tempo_de_sup',
                  'grupo','descricao','valor_de_compra','valor_de_terceiros','data']
        labels = {

            'tempo_de_instalacao' : 'Tempo de instalação ∆T INF.',
            'tempo_de_sup' : 'Tempo de suporte ∆T SUP.',
            'descricao' : 'Descricao (Que vai para o documento do termo.)',
            'data': 'Data da cotação'
        }

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
        fields = ['nome_projeto','margem','valor_infra','valor_upi','valor_upr','valor_upe']

class NameForm(forms.Form):
    project_name = forms.CharField(label='Nome do Projeto', max_length=100)