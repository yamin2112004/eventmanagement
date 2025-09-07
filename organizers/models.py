from django.db import models

class Organizer(models.Model):
   
    OrganizerName = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.OrganizerName
