from django.db import models
from django.db.models.base import Model

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null= True)

    def __str__(self):
        return self.title    