from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    nit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)