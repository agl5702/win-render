from django.contrib import admin
from .models import Equipo, Jugador, Equipo_torneo


# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display= ('nombre','detalles',)

class JugadorAdmin(admin.ModelAdmin):
    list_display= ('nombre','id_jugador','numero_ficha',)

class EquipoTorneoAdmin(admin.ModelAdmin):
    list_display= ('equipo',)


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Equipo_torneo,EquipoTorneoAdmin)
