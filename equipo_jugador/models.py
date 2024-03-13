from django.db import models

from torneos.models import Torneo

# Create your models here.
class Equipo(models.Model):
    nombre= models.CharField(max_length=45)
    logo= models.ImageField(upload_to='equipo_jugador/media/equipo',blank=True,null=True)
    torneo_equipo=models.ForeignKey(Torneo, on_delete=models.CASCADE,default=1)
    detalles= models.TextField()

    def __str__(self):
        return f'{self.nombre}'

class Jugador(models.Model):

    id_jugador= models.IntegerField(primary_key=True)
    jugador_equipo= models.ManyToManyField(Equipo, related_name='jugadores') 
    nombre= models.CharField(max_length=45)
    numero_ficha=models.IntegerField(default=0,blank=True,null=True)

    def __str__(self):
        return f'Nombre: {self.nombre} {self.jugador_equipo}'

class Equipo_torneo(models.Model):
    equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Nombre: {self.equipo.nombre}'
