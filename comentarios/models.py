from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    class Meta:
        ordering = ('data',) #Aqui ordenamos as categorias em ordem alfabética.
        verbose_name_plural = 'Comentários' #Aqui eu altero a forma como o Django vai transformar em plural as palavras que eu escrever.

    def __str__(self):
        return self.usuario.first_name