from django.urls import path, include 
from rest_framework.documentation  import include_docs_urls
from rest_framework import routers
from .views import EquipoView, JugadorView, EquipoTorneoView

router = routers.DefaultRouter()
router.register(r'equipos',EquipoView, 'equipo')
router.register(r'jugadores',JugadorView, 'jugador')
router.register(r'equipos_jugadores',EquipoTorneoView, 'equipo_torneo')



urlpatterns = [
    path('',include(router.urls) ),
    path('docs/',include_docs_urls(title='Equipo,Jugador Api')),

]
