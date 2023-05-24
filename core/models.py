from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

# Create your models here.
#Aqui criamos as características que tem na classe criada (nome, id, etc.)

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome',) #Aqui ordenamos as categorias em ordem alfabética.
        verbose_name_plural = 'Pontos Turísticos'

    def __str__(self):
        return self.nome
