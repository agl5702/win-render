#importamos desde rest_framework el serializer
from rest_framework import serializers
from .models import Torneo

#Creamos una clase 
class TorneoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Torneo
        fields = '__all__'

