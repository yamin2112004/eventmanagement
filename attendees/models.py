from django.db import models

class Attendee(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return self.name
