
# Create your views here.
from rest_framework import viewsets
from .serializer import EquipoSerializer, JugadorSerializer, EquipoTorneoSerializer
from .models import Equipo, Jugador, Equipo_torneo

# Vista crud.. 
class EquipoView(viewsets.ModelViewSet):
    serializer_class = EquipoSerializer
    queryset = Equipo.objects.all()
    
class JugadorView(viewsets.ModelViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()
    
class EquipoTorneoView(viewsets.ModelViewSet):
    serializer_class = EquipoTorneoSerializer
    queryset = Equipo_torneo.objects.all()
    
