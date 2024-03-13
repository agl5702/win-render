from django.contrib import admin
<<<<<<< HEAD
from .models import Partido
# Register your models here.



class PartidoAdmin(admin.ModelAdmin):
    list_display= ('gol_local','gol_visitante')

=======
from .models import Horario, Partido
# Register your models here.

class HorarioAdmin(admin.ModelAdmin):
    list_display= ('fecha','hora','detalles',)

class PartidoAdmin(admin.ModelAdmin):
    list_display= ('horario_partido','gol_local','gol_visitante','detalle',)

admin.site.register(Horario,HorarioAdmin)
>>>>>>> 0d6c3cac974086b0c22aab65866da3557ddd972b
admin.site.register(Partido,PartidoAdmin)
