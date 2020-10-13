from django.db import models
from empleado.models import Empleados

class Turnos (models.Model):
    """
    docstring
    """


    idTurno = models.AutoField(primary_key=True)
    dia = models.DateField( auto_now=True, auto_now_add=False)
    hora = models.TimeField( auto_now=True, auto_now_add=False)
    docEmp = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    seleccionado = models.IntegerField(0)

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
    
    def __str__(self):
        return self.idTurno
    