from rest_framework import serializers
from .models import Equipo, Jugador, Equipo_torneo

#Creamos una clase 
class EquipoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Equipo
        fields = '__all__'
    def create(self, validated_data):
        # Obtener el usuario autenticado
        usuario = self.context['request'].user
        # Asignar automáticamente el usuario al crear un nuevo torneo
        validated_data['usuario'] = usuario
        # Crear y devolver el objeto Torneo
        return Equipo.objects.create(**validated_data)  
class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Jugador
        fields = '__all__'

    def create(self, validated_data):
        # Obtener el usuario autenticado
        usuario = self.context['request'].user
        # Asignar automáticamente el usuario al crear un nuevo torneo
        validated_data['usuario'] = usuario
        # Crear y devolver el objeto Torneo
        equipos_data = validated_data.pop('jugador_equipo')
        jugador= Jugador.objects.create(**validated_data)  
        jugador.jugador_equipo.set(equipos_data)
        return jugador
class EquipoTorneoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Equipo_torneo
        fields = '__all__'
    def create(self, validated_data):
        # Obtener el usuario autenticado
        usuario = self.context['request'].user
        # Asignar automáticamente el usuario al crear un nuevo torneo
        validated_data['usuario'] = usuario
        # Crear y devolver el objeto Torneo
        return Equipo_torneo.objects.create(**validated_data)
