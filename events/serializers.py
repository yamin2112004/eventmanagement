from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        fields= '__all__'

class EventListSerializercustomize(serializers.ModelSerializer):  
    class Meta:
        model= Event
        fields= ['title']