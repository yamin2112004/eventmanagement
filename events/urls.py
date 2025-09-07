from django.urls import path
from .views import EventListView, EventCreateView, EventRetrieveView, EventUpdateView, EventDeleteView
urlpatterns = [
    
    path("events/", EventListView.as_view(), name='EventListView'),
    path("events/create", EventCreateView.as_view(), name='EventCreateView'),
    path("events/<int:pk>", EventRetrieveView.as_view(), name='EventRetrieveView'),
    path("events/<int:pk>/update/", EventUpdateView.as_view(), name='EventUpdateView'),
    path("events/<int:pk>/delete/", EventDeleteView.as_view(), name='EventDeleteView')

]
