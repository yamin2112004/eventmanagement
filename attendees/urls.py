from django.urls import path
from .views import AttendeeListView, AttendeeCreateView, AttendeeRetrieveView,  AttendeeUpdateView, AttendeeDeleteView

urlpatterns = [
    path("attendees/", AttendeeListView.as_view(), name="AttendeeListView"),
    path("attendees/create", AttendeeCreateView.as_view(), name='AttendeeCreateView'),
    path("attendees/<int:pk>", AttendeeRetrieveView.as_view(), name='AttendeeRetrieveView'),
    path("attendees/<int:pk>/update/", AttendeeUpdateView.as_view(), name='AttendeeUpdateView'),
    path("attendees/<int:pk>/delete/", AttendeeDeleteView.as_view(), name='AttendeeDeleteView')
]
