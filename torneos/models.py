
# Modelo de Torneos
from typing import Iterable
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


UserModel = get_user_model()

# modelo
class Torneo(models.Model):
    
    titulo= models.CharField(max_length=200)
    descripcion= models.TextField()
    fecha_inicio= models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(UserModel, on_delete=models.CASCADE,default=get_user_model())

    def get_context_data(self, **kwargs):
        # Llama al método de la clase base para obtener el contexto inicial
        context = super().get_context_data(**kwargs)
        
        # Obtén el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        torneos = Torneo.objects.filter(usuario=user)

        # Agrega los torneos filtrados al contexto
        context['torneos'] = torneos

        return context
    def save(self, *args, **kwargs):
        # Si el usuario no está establecido y la instancia no ha sido guardada previamente
        if not self.usuario_id and not self.pk:
            # Establecer el usuario actual como el creador del torneo
            self.usuario = self._get_default_user()
        super().save(*args, **kwargs)

    def _get_default_user(self):
        # Obtener el usuario actual o el usuario predeterminado (si no hay uno autenticado)
        return getattr(self, 'usuario', None) or UserModel.objects.get(pk=settings.DEFAULT_USER_ID)

    def __str__(self):
        return self.titulo


