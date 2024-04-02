
# Create your views here.
from rest_framework import viewsets
from .serializer import EquipoSerializer, JugadorSerializer, EquipoTorneoSerializer
from .models import Equipo, Jugador, Equipo_torneo
from rest_framework.permissions import IsAuthenticated

# Vista crud.. 
class EquipoView(viewsets.ModelViewSet):
    serializer_class = EquipoSerializer
    queryset = Equipo.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Obtener el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        queryset = Equipo.objects.filter(usuario=user)

        return queryset

class JugadorView(viewsets.ModelViewSet):
    serializer_class = JugadorSerializer
    queryset = Jugador.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Obtener el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        queryset = Jugador.objects.filter(usuario=user)

        return queryset

class EquipoTorneoView(viewsets.ModelViewSet):
    serializer_class = EquipoTorneoSerializer
    queryset = Equipo_torneo.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Obtener el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        queryset = Equipo_torneo.objects.filter(usuario=user)

        return queryset
