from django.forms import ModelForm
from .models import Contatos, ListaMaterial

class FormularioContato(ModelForm):
    class Meta:
        model = Contatos
        fields = ['nome','fabricante','descricao','valor']

class FormularioLista(ModelForm):
    class Meta:
        model = ListaMaterial
        fields = ['produto','quantidade']
