from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=80)
    endereco = models.CharField(max_length=150)
    data_nascimento = models.CharField(max_length=10)
    escolaridade =  models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL, null=True)

#chave estrangeira - número de cliente para categoria, link para categoria
# 1 - N
    def __str__(self):
        return self.nome + " " + self.sobrenome
# Create your models here.
