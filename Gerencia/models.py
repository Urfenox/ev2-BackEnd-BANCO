from django.db import models
import time

# Create your models here.

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    cantidad = models.IntegerField(null=False)
    fecha_ingreso = models.DateField(null=False, default=time.strftime("%Y-%m-%d", time.localtime()))
