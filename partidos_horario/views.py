
# Create your views here.
from rest_framework import viewsets
from .serializer import PartidoSerializer
from .models import Partido

# Vista crud.. 

    
class PartidoView(viewsets.ModelViewSet):
    serializer_class = PartidoSerializer
    queryset = Partido.objects.all()
