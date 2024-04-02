from django.db import models
from equipo_jugador.models import Equipo
from django.conf import settings
from django.contrib.auth import get_user_model
UserModel = get_user_model()
# Create your models here.




class Partido(models.Model):
    usuario = models.ForeignKey(UserModel, on_delete=models.CASCADE,default=get_user_model())
    equipo_local = models.ManyToManyField(Equipo, related_name='equipos_locales')
    equipo_visitante = models.ManyToManyField(Equipo, related_name='equipos_visitantes')

    gol_local= models.IntegerField(default=0)
    gol_visitante= models.IntegerField(default=0)
    fecha= models.DateField()
    hora= models.TimeField()
    
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
        return f'{self.gol_local} {self.gol_visitante}'
