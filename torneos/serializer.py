#importamos desde rest_framework el serializer
from rest_framework import serializers
from .models import Torneo

#Creamos una clase 
class TorneoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Torneo
        fields = '__all__'

    def create(self, validated_data):
        # Obtener el usuario autenticado
        usuario = self.context['request'].user
        # Asignar automáticamente el usuario al crear un nuevo torneo
        validated_data['usuario'] = usuario
        # Crear y devolver el objeto Torneo
        return Torneo.objects.create(**validated_data)