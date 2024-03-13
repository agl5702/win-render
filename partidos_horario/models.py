from django.db import models
from equipo_jugador.models import Equipo

# Create your models here.

class Horario(models.Model):
    fecha= models.DateField()
    hora= models.TimeField()
    detalles= models.CharField(max_length=100)
    
    def __str__(self):
        return f'Fecha: {self.fecha}'



class Partido(models.Model):
    equipo_local = models.ManyToManyField(Equipo, related_name='equipos_locales')
    equipo_visitante = models.ManyToManyField(Equipo, related_name='equipos_visitantes')

    gol_local= models.IntegerField(default=0)
    gol_visitante= models.IntegerField(default=0)
    fecha= models.DateField()
    hora= models.TimeField()

    horario_partido= models.ForeignKey(Horario, on_delete=models.CASCADE)
    gol_local= models.IntegerField(default=0)
    gol_visitante= models.IntegerField(default=0)
    detalle= models.TextField()
    

    def __str__(self):
        return f'{self.gol_local} {self.gol_visitante}'
