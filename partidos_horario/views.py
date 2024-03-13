
# Create your views here.
from rest_framework import viewsets
<<<<<<< HEAD
from .serializer import PartidoSerializer
from .models import Partido

# Vista crud.. 

=======
from .serializer import HorarioSerializer,PartidoSerializer
from .models import Horario, Partido

# Vista crud.. 
class HorarioView(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    queryset = Horario.objects.all()
>>>>>>> 0d6c3cac974086b0c22aab65866da3557ddd972b
    
class PartidoView(viewsets.ModelViewSet):
    serializer_class = PartidoSerializer
    queryset = Partido.objects.all()
