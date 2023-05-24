from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

# Create your models here.
#Aqui definimos as características que nossa classe terá (nome, id, etc.)

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    class Meta:
        ordering = ('nome',) #Aqui ordenamos as categorias em ordem alfabética.
        verbose_name_plural = 'Pontos Turísticos'

    def __str__(self):
        return self.nome
