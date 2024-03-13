
# Create your views here.
from rest_framework import viewsets
from .serializer import TablaPosicioneSerializer,Tabla_PartidoSerializer
from .models import TablaPosiciones, Tabla_Partidos

# Vista crud.. 
class TablaPosicionesView(viewsets.ModelViewSet):
    serializer_class = TablaPosicioneSerializer
    queryset = TablaPosiciones.objects.all()
    
class Tabla_PartidosView(viewsets.ModelViewSet):
    serializer_class = Tabla_PartidoSerializer
    queryset = Tabla_Partidos.objects.all()
