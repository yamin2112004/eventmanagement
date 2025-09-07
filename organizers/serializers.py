from rest_framework import serializers
from .models import Organizer

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Organizer
        fields= '__all__'

class OrganizerSerializercustomize(serializers.ModelSerializer):  
    class Meta:
        model= Organizer
        fields= ['title']