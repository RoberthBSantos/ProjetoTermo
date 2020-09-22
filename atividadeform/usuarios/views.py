from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.base import View
from contatos.models import Perfil
from usuarios.forms import RegistrarUsuarioForm, FormularioUser


def RegistrarUsuarioView(request):
    form = FormularioUser(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_projetos')

    return render(request, 'registrar.html', {'form': form})
