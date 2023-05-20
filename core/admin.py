from django.contrib import admin

# Register your models here.

#Aqui, pelo que entendi, registramos as API que criamos, para que elas façam parte do servidor que criamos.
from .models import PontoTuristico

admin.site.register(PontoTuristico)