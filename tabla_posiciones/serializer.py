from rest_framework import serializers
from .models import TablaPosiciones, Tabla_Partidos

#Creamos una clase 
class TablaPosicioneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= TablaPosiciones
        fields = '__all__'
        
class Tabla_PartidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Tabla_Partidos
        fields = '__all__'