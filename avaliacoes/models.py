from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    avaliacao = models.IntegerField(min_value=1, max_value=5)
    data = models.DateTimeField(auto_now_add=True)

    