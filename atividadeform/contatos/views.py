from django.shortcuts import render, redirect, get_object_or_404
from .models import Contatos, ListaMaterial
from .forms import FormularioContato, FormularioLista

def listar_contatos(request):
    busca = request.GET.get('pesquisa',None)

    if busca:
        # contatos = Contatos.objects.all()
        contatos = Contatos.objects.filter(nome__icontains = busca) or Contatos.objects.filter(fabricante__icontains = busca)
    else:
        contatos = Contatos.objects.all()

    return render(request, 'contatos.html', {'contatos' : contatos})

# def listar_produtos(request):
#     busca = request.GET.get('pesquisa', None)
#
#     produtos = ListaMaterial.objects.all()
#
#     return render(request, 'formulario_lista.html')

def novo_contato(request):
    form = FormularioContato(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_contatos')

    return  render(request, 'formulario_contato.html', {'form' : form})

def atualizar_contato(request, id):
    contato = get_object_or_404(Contatos, pk=id)
    form = FormularioContato(request.POST or None, instance = contato)

    if form.is_valid():
        form.save()
        return redirect('lista_contatos')

    return render(request,'formulario_contato.html', {'form' : form})

def excluir_produto(request,id):
    produto = get_object_or_404(Contatos, id =  id)
    form = FormularioContato(request.POST or None, request.FILES or None, instance = produto)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_contatos')

    # if request.method is not 'POST':
    #     post_delete=Contatos.objects.filter(id=id)
    #     post_delete.delete()
    #     return redirect('lista_contatos')

    return render(request, 'confirmar_delete_produto.html', {'produto': produto})

def excluir_prod_lista(request,id):
    produto = get_object_or_404(ListaMaterial, id = id)
    form = FormularioLista(request.POST or None)
    produtos = ListaMaterial.objects.all()
    contatos = Contatos.objects.all()

    if request.method is not 'POST':
        post_delete=ListaMaterial.objects.filter(id=id)
        post_delete.delete()
        produtos = ListaMaterial.objects.all()
        contatos = Contatos.objects.all()
        return render(request, 'formulario_lista.html', {'form': form, 'produtos': produtos, 'contatos': contatos})
    return render(request, 'formulario_lista.html', {'form': form, 'produtos': produtos, 'contatos': contatos})

def nova_lista(request):
    form = FormularioLista(request.POST or None)

    if form.is_valid():
        form.save()
        produtos = ListaMaterial.objects.all()
        contatos = Contatos.objects.all()
        return render(request, 'formulario_lista.html', {'form': form,'produtos':produtos, 'contatos':contatos})

    produtos = ListaMaterial.objects.all()
    contatos = Contatos.objects.all()

    return render(request, 'formulario_lista.html', {'form': form,'produtos':produtos, 'contatos':contatos})