from django.db import models

class Venda(models.Model):
    nome_imovel = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8,decimal_places=4)
    data_venda = models.DateField(auto_now=True)
    quantidade = models.IntegerField()
    descricao = models.TextField(max_length=150)
    foto_venda = models.ImageField(upload_to='Imovel',blank=True, null=True)


    def __str__(self):
        return self.nome_imovel
    
class Reserva(models.Model):
    imovel = models.CharField(max_length=100)
    dada_reserva = models.DateField(auto_now=True)
    descricao = models.TextField(max_length=150)
    foto_reserva = models.ImageField(upload_to='Reserva',blank=True, null=True)
    

    def __str__(self):
        return self.imovel


# Create your models here.
