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
    modelo = models.CharField(max_length=50,blank=True,null=True)
    grupo = models.ForeignKey(Grupos,null=True,blank=True, on_delete= models.PROTECT)
    descricao = models.TextField(null= True,blank= True, max_length=2000, default="")
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fornecedor = models.ForeignKey(Fornecedor,null=True, blank=True, on_delete = models.PROTECT)
    data = models.DateTimeField()

    class Meta:
        ordering = ('nome',)


    def __str__(self):
        return self.nome + ' ' + self.fabricante

class Projeto (models.Model):
    nome_projeto = models.CharField(max_length= 300)

    def __str__(self):
        return str(self.nome_projeto)

class ListaMaterial (models.Model):
    quantidade = models.IntegerField(null=False, blank=False)
    produto = models.ForeignKey(Produtos, null=True, blank= True, on_delete=models.PROTECT)
    projeto = models.ForeignKey(Projeto,null=True, on_delete=models.PROTECT)

    def __str__(self):
         return str(self.quantidade)+ ' ' +  self.produto.nome


    def __str__(self):
        return self.nome_projeto

class DocFiles(models.Model):
    docupload= models.FileField(max_length=500)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


