from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class Hello(models.Model):
    name = models.CharField(max_length = 10, null = True)
    
    def __str__(self):
        return self.name