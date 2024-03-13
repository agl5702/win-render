from django.contrib import admin
from .models import TablaPosiciones,Tabla_Partidos
# Register your models here.

class TablaPosicionesAdmin(admin.ModelAdmin):
    list_display=('puntos','victorias','derrotas','goles_a_favor','goles_en_contra',)

# class Tabla_PartidosAdmin(admin.ModelAdmin):
#     list_display=('tablas_partidos.puntos','partido.hora')


admin.site.register(TablaPosiciones,TablaPosicionesAdmin)
admin.site.register(Tabla_Partidos)