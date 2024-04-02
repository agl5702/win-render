from rest_framework import serializers

from .models import Partido


        
class PartidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Partido
        fields = '__all__'
        

    def create(self, validated_data):
        # Obtener el usuario autenticado
        usuario = self.context['request'].user
        # Asignar automáticamente el usuario al crear un nuevo torneo

        validated_data['usuario'] = usuario
        equipo_local = validated_data.pop('equipo_local', None)
        equipo_visitante = validated_data.pop('equipo_visitante', None)

        partido= Partido.objects.create(**validated_data)  

        if equipo_local is not None:
            partido.equipo_local.set(equipo_local)
        if equipo_visitante is not None:
            partido.equipo_visitante.set(equipo_visitante)

        return partido
        # Crear y devolver el objeto Torneo

