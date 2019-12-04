from django.db import models
from django.contrib.auth.models import User

class Regiao_corporal(models.Model):
	nome=models.CharField(max_length=100)

class Tempo_repeticao(models.Model):
	nome=models.CharField(max_length=100)

class Intervalo_treinos(models.Model):
	nome=models.CharField(max_length=100)

class Treino(models.Model):
	nome=models.CharField(max_length=100)
	dia_semana = models.CharField(max_length=100)
	regiao=models.ManyToManyField(Regiao_corporal)
	tempo_repaticao=models.ForeignKey(Tempo_repeticao,on_delete=models.CASCADE,null=True)
	intervalo_treinos=models.ForeignKey(Intervalo_treinos,on_delete=models.CASCADE,null=True)

"""

dia da semana 
nome do treino
região corporal
tempo/repetição
intervalo entre os treinos

"""