from django.db import models

# Create your models here.

class Contatos(models.Model):
    nome = models.CharField(max_length= 30)
    fabricante = models.CharField(max_length = 30)
    descricao = models.TextField(null= True,blank= True, max_length=1000, default="")
    valor = models.FloatField(null=False, default=0)

    def __str__(self):
        return self.nome + ' ' + self.fabricante

class ListaMaterial (models.Model):
    quantidade = models.IntegerField(null=False, blank=False)
    produto = models.ForeignKey(Contatos, null=True, blank= True, on_delete=models.PROTECT)

    def __str__(self):
        return self.quantidade