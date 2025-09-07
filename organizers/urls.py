

from django.urls import path
from .views import OrganizerListView, OrganizerCreateView, OrganizerRetrieveView, OrganizerUpdateView, OrganizerDeleteView
urlpatterns = [
    
    path("organizers/", OrganizerListView.as_view(), name='OrganizerListView'),
    path("organizers/create", OrganizerCreateView.as_view(), name='OrganizerCreateView'),
    path("organizers/<int:pk>", OrganizerRetrieveView.as_view(), name='EventRetrieveView'),
    path("organizers/<int:pk>/update/", OrganizerUpdateView.as_view(), name='EventUpdateView'),
    path("organizers/<int:pk>/delete/", OrganizerDeleteView.as_view(), name='OrganizerDeleteView')

]
