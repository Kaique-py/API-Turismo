from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao

# Create your models here.
#Aqui, ao que entendi, criamos os endpoints que queremos ter no site e, para cada um deles, criamos suas características

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)

    class Meta:
        ordering = ('nome',) #Aqui ordenamos as categorias em ordem alfabética.
        verbose_name_plural = 'Pontos Turísticos'

    def __str__(self):
        return self.nome
