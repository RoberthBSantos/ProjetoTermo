from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, blank=False, null=False)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.razao_social


class Grupos(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produtos(models.Model):
    nome = models.CharField(max_length=300)
    fabricante = models.CharField(max_length=30, blank=True, default="")
    modelo = models.CharField(max_length=50, blank=True, default="")
    unidade = models.CharField(max_length=15, blank=True, default='UND')
    grupo = models.ForeignKey(Grupos, null=True, blank=True, on_delete=models.PROTECT)
    descricao = models.TextField(null=True, blank=True, default="")
    valor_de_compra = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fornecedor = models.ForeignKey(Fornecedor, null=True, blank=True, on_delete=models.PROTECT)
    tempo_de_instalacao = models.IntegerField(blank=True, default=1)
    tempo_de_sup = models.IntegerField(blank=True, default=0)
    valor_de_terceiros = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    data = models.DateTimeField()

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome + ' ' + self.modelo + ' ' + self.fabricante


class SubItem(models.Model):
    item = models.ForeignKey(Produtos,blank= True,related_name='produto', null= True, on_delete= models.CASCADE)
    sub = models.ForeignKey(Produtos,blank= True, null= True, on_delete= models.CASCADE)
    quantidade = models.IntegerField(blank=True, default=0)


class TipoProjeto(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return  self.nome

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=300)
    margem = models.IntegerField(null=True, blank=True)
    valor_infra = models.IntegerField(default=40)
    valor_sup = models.DecimalField(default=64.00, decimal_places=2, max_digits=5)
    valor_upi = models.DecimalField(default=0.70, decimal_places=2, max_digits=5)
    valor_upr = models.DecimalField(default=0.80, decimal_places=2, max_digits=5)
    valor_upe = models.DecimalField(default=0.90, decimal_places=2, max_digits=5)
    user = models.ForeignKey(User, null=True, related_name='owner', on_delete=models.PROTECT)
    tipo_de_projeto = models.ForeignKey(TipoProjeto,null=True,on_delete=models.PROTECT)
    convidados = models.ManyToManyField(User)

    def __str__(self):
        return str(self.nome_projeto)


class ListaMaterial(models.Model):
    quantidade = models.IntegerField(null=False, blank=False)
    produto = models.ForeignKey(Produtos, null=True, blank=True, on_delete=models.PROTECT)
    projeto = models.ForeignKey(Projeto, null=True, on_delete=models.CASCADE)


    @property
    def custo_produto(self):
        sub_itens = SubItem.objects.filter(item = self.produto)
        soma_itens = 0
        for i in sub_itens:
            soma_itens += i.sub.valor_de_compra * i.quantidade
        soma_itens += self.produto.valor_de_compra


        total = ((self.projeto.margem / 100) * float(soma_itens)) + float(
            soma_itens)



        if self.produto.grupo.nome == 'INFRAESTRUTURA' or self.produto.grupo.nome == 'SERVIÇOS DE INFRAESTRUTURA':
            pontos = total / float(self.projeto.valor_upi)
            pontos = round(pontos + 0.5)
            total = pontos * self.projeto.valor_upi

        elif self.produto.grupo.nome == 'REDE DE DADOS E ENERGIA' or self.produto.grupo.nome == 'SEGURANÇA':
            pontos = total / float(self.projeto.valor_upe)
            pontos = round(pontos + 0.5)
            total = pontos * self.projeto.valor_upe

        else:
            pontos = total / float(self.projeto.valor_upr)
            pontos = round(pontos + 0.5)
            total = pontos * self.projeto.valor_upr

        return total

    @property
    def custo_servico(self):
        total = ((self.produto.tempo_de_instalacao / 60) * float(self.projeto.valor_infra) +
                 (self.produto.tempo_de_sup / 60) * float(self.projeto.valor_sup))

        if self.produto.grupo.nome == 'INFRAESTRUTURA' or self.produto.grupo.nome == 'SERVIÇOS DE INFRAESTRUTURA':
            pontos = total / float(self.projeto.valor_upi)
            pontos = round(pontos + 0.5)
            total = pontos * self.projeto.valor_upi

        elif self.produto.grupo.nome == 'REDE DE DADOS E ENERGIA' or self.produto.grupo.nome == 'SEGURANÇA':
            pontos = total / float(self.projeto.valor_upe)
            pontos = round(pontos + 0.5)
            total = pontos * self.projeto.valor_upe

        else:
            pontos = total / float(self.projeto.valor_upr)
            pontos = round(pontos + 0.5)
            total = pontos * self.projeto.valor_upr

        return total

    @property
    def custo_venda(self):
        total = self.custo_servico + self.custo_produto + self.produto.valor_de_terceiros

        return total



    @property
    def subtotal(self):
        subtotal = (self.custo_venda * self.quantidade) + self.produto.valor_de_terceiros
        return subtotal

    def __str__(self):
        return self.produto.nome

    @property
    def pontos(self):
        if self.produto.grupo.nome == 'INFRAESTRUTURA' or self.produto.grupo.nome == 'SERVIÇOS DE INFRAESTRUTURA':
            total = float(self.custo_venda) / float(self.projeto.valor_upi)
            print (total)
            return round(total)
        elif self.produto.grupo.nome == 'REDE DE DADOS E ENERGIA' or self.produto.grupo.nome == 'SEGURANÇA':
            total = float(self.custo_venda) / float(self.projeto.valor_upe)
            return round(total)
        else:
            total = float(self.custo_venda) / float(self.projeto.valor_upr)
            return round(total)


class DocFiles(models.Model):
    docupload = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    # sem email
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)

    usuario = models.OneToOneField(User, related_name="perfil",
                                   on_delete=models.CASCADE)

    @property
    def email(self):
        return self.usuario.email

