from django.shortcuts import render
from .models import Attendee 
from .serializers import AttendeeSerializer, AttendeeSerializercustomize
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class AttendeeListView(generics.ListAPIView):
    queryset =Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_class= [IsAuthenticated]
    
class AttendeeCreateView(generics.CreateAPIView):
    queryset =Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_class= [IsAuthenticated]
    
class AttendeeRetrieveView(generics.RetrieveAPIView):
    queryset =Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_class= [IsAuthenticated]
    
    
        
class AttendeeUpdateView(generics.UpdateAPIView):
    queryset =Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_class= [IsAuthenticated]
    
        
class AttendeeDeleteView(generics.DestroyAPIView):
    queryset =Attendee.objects.all()
    serializer_class = AttendeeSerializer
