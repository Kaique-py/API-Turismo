from django.db import models
from comentarios.models import Comentario

# Create your models here.

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    comentarios = models.ManyToManyField(Comentario)

    class Meta:
        ordering = ('nome',) #Aqui ordenamos as categorias em ordem alfabética.
        verbose_name_plural = 'Atrações'

    def __str__(self):
        return self.nome
    