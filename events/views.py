from django.shortcuts import render
from .models import Event 
from .serializers import EventSerializer, EventListSerializercustomize
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class EventListView(generics.ListAPIView):
    queryset =Event.objects.all()
    serializer_class = EventSerializer
    permission_class= [IsAuthenticated]
      
    
class EventCreateView(generics.CreateAPIView):
    queryset =Event.objects.all()
    serializer_class = EventSerializer
    permission_class= [IsAuthenticated]
    
class EventRetrieveView(generics.RetrieveAPIView):
    queryset =Event.objects.all()
    serializer_class = EventSerializer
    permission_class= [IsAuthenticated]
    
    
        
class EventUpdateView(generics.UpdateAPIView):
    queryset =Event.objects.all()
    serializer_class = EventSerializer
    permission_class= [IsAuthenticated]
    
        
class EventDeleteView(generics.DestroyAPIView):
    queryset =Event.objects.all()
    serializer_class = EventSerializer
    