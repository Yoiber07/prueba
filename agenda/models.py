from django.db import models
from turno.models import Turnos
from cliente.models import Clientes

class Agenda(models.Model):
    """
    docstring
    """
    idAgenda = models.AutoField(primary_key=True)
    idTurno = models.ForeignKey(Turnos,  on_delete=models.CASCADE)
    docCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150,blank=False,null=False)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Angendas"
    
    def __str__(self):
        return self.idAgenda
    