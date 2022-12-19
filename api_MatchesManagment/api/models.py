from django.db import models

# Create your models here.

class posiciones(models.Model):
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=50)
