
# Modelo de Torneos
from django.db import models




# modelo
class Torneo(models.Model):
    
    titulo= models.CharField(max_length=200)
    descripcion= models.TextField()
    fecha_inicio= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo


