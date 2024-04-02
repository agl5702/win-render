from django.db import models
from torneos.models import Torneo
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.
class Equipo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=get_user_model)
    nombre= models.CharField(max_length=45)
    logo= models.ImageField(upload_to='equipo_jugador/media/equipo',blank=True,null=True)
    torneo_equipo=models.ForeignKey(Torneo, on_delete=models.CASCADE,default=1)
    detalles= models.TextField()

    def get_context_data(self, **kwargs):
        # Llama al método de la clase base para obtener el contexto inicial
        context = super().get_context_data(**kwargs)
        
        # Obtén el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        equipos = Equipo.objects.filter(usuario=user)

        # Agrega los torneos filtrados al contexto
        context['equipos'] = equipos

        return context
    
    def __str__(self):
        return f'{self.nombre}'

class Jugador(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=get_user_model)
    id_jugador= models.IntegerField(primary_key=True)
    jugador_equipo= models.ManyToManyField(Equipo, related_name='jugadores') 
    nombre= models.CharField(max_length=45)
    numero_ficha=models.IntegerField(default=0,blank=True,null=True)

    def get_context_data(self, **kwargs):
        # Llama al método de la clase base para obtener el contexto inicial
        context = super().get_context_data(**kwargs)
        
        # Obtén el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        jugadores = Jugador.objects.filter(usuario=user)

        # Agrega los torneos filtrados al contexto
        context['jugadores'] = jugadores

        return context

    def __str__(self):
        return f'Nombre: {self.nombre} {self.jugador_equipo}'

class Equipo_torneo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=get_user_model)
    equipo= models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def get_context_data(self, **kwargs):
        # Llama al método de la clase base para obtener el contexto inicial
        context = super().get_context_data(**kwargs)
        
        # Obtén el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        equipos_torneos = Equipo_torneo.objects.filter(usuario=user)

        # Agrega los torneos filtrados al contexto
        context['equipos_torneos'] = equipos_torneos

        return context
    def __str__(self):
        return f'Nombre: {self.equipo.nombre}'
