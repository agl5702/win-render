from django.contrib import admin

from .models import Partido
# Register your models here.



class PartidoAdmin(admin.ModelAdmin):
    list_display= ('gol_local','gol_visitante')

admin.site.register(Partido,PartidoAdmin)
