from django.db import models
from equipo_jugador.models import Equipo
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.




class Partido(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    equipo_local = models.ManyToManyField(Equipo, related_name='equipos_locales')
    equipo_visitante = models.ManyToManyField(Equipo, related_name='equipos_visitantes')

    gol_local= models.IntegerField(default=0)
    gol_visitante= models.IntegerField(default=0)
    fecha= models.DateField()
    hora= models.TimeField()


    def __str__(self):
        return f'{self.gol_local} {self.gol_visitante}'
