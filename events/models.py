from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=20, null=False)
    date = models.DateField(db_column="D_O_P")  # maps old column
    description = models.TextField(db_column="Description")  # maps old column
    active = models.BooleanField(null=False)

    def __str__(self):
        return self.title
