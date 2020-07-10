from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.id}:{self.name}:{self.active}'