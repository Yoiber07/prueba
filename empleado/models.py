from django.db import models
from servicio.models import Servicios

# Create your models here.

class Empleados(models.Model):
    """
    docstring
    """
    docmp = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=70,blank=False, null=False)
    primerApellido = models.CharField(max_length=70,blank=False, null=False)
    segundoApellido = models.CharField(max_length=70,blank=False, null=False)
    email = models.CharField(max_length=70,blank=False, null=False)
    celular = models.CharField(max_length=70,blank=False, null=False)
    fechaNacimiento = models.DateField(auto_now=True, auto_now_add=False)
    # TODO: ENPLEADOS
    idServicio=models.ForeignKey(Servicios,  on_delete=models.CASCADE)
    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"
    def __str__(self):
        return self.nombres


