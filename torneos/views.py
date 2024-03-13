
from rest_framework import viewsets
from .serializer import TorneoSerializer
from .models import Torneo

# Vista crud.. 
class TorneoView(viewsets.ModelViewSet):
    serializer_class = TorneoSerializer
    queryset = Torneo.objects.all()





