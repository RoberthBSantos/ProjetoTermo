from django.db import models

# Create your models here.


class Fornecedor(models.Model):
    razao_social = models.CharField(max_length = 50)
    telefone = models.IntegerField(blank= True, null= True)

    def __str__(self):
        return self.razao_social

class Grupos (models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length= 300)
    fabricante = models.CharField(max_length = 30)
    modelo = models.CharField(max_length=50,blank=True,default="")
    unidade = models.CharField(max_length=15,blank=True,default='UND')
    grupo = models.ForeignKey(Grupos,null=True,blank=True, on_delete= models.PROTECT)
    descricao = models.TextField(null= True,blank= True, max_length=2000, default="")
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fornecedor = models.ForeignKey(Fornecedor,null=True, blank=True, on_delete = models.PROTECT)
    tempo_de_instalacao = models.IntegerField(blank=True,default=1)
    data = models.DateTimeField()

    class Meta:
        ordering = ('nome',)


    def __str__(self):
        return self.nome + ' ' + self.fabricante

class Projeto (models.Model):
    nome_projeto = models.CharField(max_length= 300)
    margem = models.IntegerField(null=True,blank=True)
    valor_infra = models.IntegerField(default=40)

    def __str__(self):
        return str(self.nome_projeto)

class ListaMaterial (models.Model):
    quantidade = models.IntegerField(null=False, blank=False)
    produto = models.ForeignKey(Produtos, null=True, blank= True, on_delete=models.PROTECT)
    projeto = models.ForeignKey(Projeto,null=True, on_delete=models.PROTECT)

    @property
    def custo_produto(self):
        total = ((self.projeto.margem/100) * float(self.produto.valor)) + float(self.produto.valor)

        return total

    @property
    def custo_servico(self):
        total = (self.produto.tempo_de_instalacao / 60) * float(self.projeto.valor_infra)

        return total

    @property
    def custo_venda(self):
        total = ((self.produto.tempo_de_instalacao / 60) * float(self.projeto.valor_infra)) \
                + (((self.projeto.margem / 100) * float(self.produto.valor)) + float(self.produto.valor))

        return total

    def __str__(self):
        return self.produto.nome

class DocFiles(models.Model):
    docupload= models.FileField(max_length=500)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


