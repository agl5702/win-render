from rest_framework import serializers
from .models import Partido

#Creamos una clase 

        
class PartidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Partido
        fields = '__all__'
        

        