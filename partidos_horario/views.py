
# Create your views here.
from rest_framework import viewsets

from .serializer import PartidoSerializer
from .models import Partido
from rest_framework.permissions import IsAuthenticated


    
class PartidoView(viewsets.ModelViewSet):
    serializer_class = PartidoSerializer
    queryset = Partido.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Obtener el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        queryset = Partido.objects.filter(usuario=user)

        return queryset