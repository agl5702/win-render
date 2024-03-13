from django.contrib import admin
from .models import Torneo
# Register your models here.

class TorneoAdmin(admin.ModelAdmin):
    list_display=('titulo','descripcion','fecha_inicio')

admin.site.register(Torneo, TorneoAdmin)
