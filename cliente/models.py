from django.db import models

# Create your models here.
class Clientes(models.Model):
    """
    tabla clientes
    """
    docCliente = models.IntegerField("Identificacion",primary_key=True)
    nombres = models.CharField("Nombres" ,max_length=70,blank=False, null=False)
    primerApellido = models.CharField("Primer Apellido", max_length=70,blank=False, null=False)
    segundoApellido = models.CharField("Segundo Apellido", max_length=70,blank=False, null=False)
    email = models.EmailField(" Correo",max_length=150,blank=False, null=False)
    celular = models.CharField("Celular ", max_length=12,blank=False, null=False)
    fechaNacimiento = models.DateField()

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombres

    
    

