from django.forms import ModelForm, DateInput
from phone_field import PhoneNumber
from .models import Produtos, ListaMaterial, Fornecedor

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