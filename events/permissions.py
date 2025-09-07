# events/permissions.py
from rest_framework.permissions import BasePermission

class IsOrganizer(BasePermission):
    def has_permission(self, request, view):
        # Check if user is logged in and linked to an Organizer profile
        return request.user.is_authenticated and hasattr(request.user, 'organizer')

class IsAttendee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'attendee')