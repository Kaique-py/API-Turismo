from django.db import models

# Create your models here.
#Aqui, ao que entendi, criamos os endpoints que queremos ter no site e, para cada um deles, criamos suas características

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(default='')
    aprovado = models.BooleanField(default=False)

def __str__(self):
    return self.nome
