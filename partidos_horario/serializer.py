from rest_framework import serializers
<<<<<<< HEAD
from .models import Partido

#Creamos una clase 

=======
from .models import Horario, Partido

#Creamos una clase 
class HorarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Horario
        fields = '__all__'
>>>>>>> 0d6c3cac974086b0c22aab65866da3557ddd972b
        
class PartidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Partido
        fields = '__all__'
        

        