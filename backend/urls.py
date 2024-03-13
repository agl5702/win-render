from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls ),
    path('torneoapp/', include('torneos.urls')),
    path('equipo_jugador/', include('equipo_jugador.urls')),
    path('partidos_horarios/', include('partidos_horario.urls')),
    path('tabla_posiciones/', include('tabla_posiciones.urls')),
]