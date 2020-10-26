from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = \
            User.objects.filter(username=self.cleaned_data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuário já existente.')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors =  self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,
                                forms.utils.ErrorList())
        errors.append(message)

class FormularioUser(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username', 'password1', 'password2',]