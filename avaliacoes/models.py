from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.DecimalField(default=1, max_digits=3, decimal_places=2)
    comentario = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('data',) #Aqui ordenamos as categorias em ordem alfabética.
        verbose_name_plural = 'Avaliações' #Aqui eu altero a forma como o Django vai transformar em plural as palavras que eu escrever.

    def __str__(self):
        return self.usuario.first_name
    

