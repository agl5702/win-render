from rest_framework import viewsets, filters
from .serializer import TorneoSerializer
from .models import Torneo
from rest_framework.permissions import IsAuthenticated

class TorneoView(viewsets.ModelViewSet):
    serializer_class = TorneoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Torneo.objects.all()
   

    
    
    def get_queryset(self):
        # Obtener el usuario autenticado
        user = self.request.user

        # Filtrar los torneos para que solo incluyan aquellos asociados con el usuario autenticado
        queryset = Torneo.objects.filter(usuario=user)

        return queryset
