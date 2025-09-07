from django.shortcuts import render
from .models import Organizer 
from .serializers import OrganizerSerializer, OrganizerSerializercustomize
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class OrganizerListView(generics.ListAPIView):
    queryset =Organizer.objects.all()
    serializer_class = OrganizerSerializer
    permission_class= [IsAuthenticated]
    
class OrganizerCreateView(generics.CreateAPIView):
    queryset =  Organizer.objects.all()
    serializer_class = OrganizerSerializer
    permission_class= [IsAuthenticated]
    
class OrganizerRetrieveView(generics.RetrieveAPIView):
    queryset =Organizer.objects.all()
    serializer_class = OrganizerSerializer
    permission_class= [IsAuthenticated]
    
    
        
class OrganizerUpdateView(generics.UpdateAPIView):
    queryset =Organizer.objects.all()
    serializer_class = OrganizerSerializer
    permission_class= [IsAuthenticated]
    
        
class OrganizerDeleteView(generics.DestroyAPIView):
    queryset =Organizer.objects.all()
    serializer_class = OrganizerSerializer
