from django.db import models

class ImovelAluguel(models.Model):
    nome_imovel = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    disponibilidade_inicio = models.DateField(max_length=100)
    disponibilidade_fim = models.DateField(max_length=100)
    preco_mensal = models.DecimalField(max_digits=8,decimal_places=4)
    ativo = models.BooleanField(default=True)
    foto_aluguel = models.ImageField(upload_to='Imovel',blank=True, null=True)
    def __str__(self):
        return self.nome_imovel
    
class Contrato(models.Model):
    nome_cliente = models.CharField(max_length=100)
    imovel = models.CharField(max_length=100)
    data_inicio = models.DateField(max_length=100)
    data_fim = models.DateField(max_length=100)
    ativo = models.BooleanField(default=True)
    valor_contrato = models.FileField(upload_to='contratos', blank=True, null=True)

    def __str__(self):
        return self.nome_cliente


 



