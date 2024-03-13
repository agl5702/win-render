from rest_framework import serializers
from .models import Equipo, Jugador, Equipo_torneo

#Creamos una clase 
class EquipoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Equipo
        fields = '__all__'
        
class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Jugador
        fields = '__all__'
        
class EquipoTorneoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Equipo_torneo
        fields = '__all__'
        
