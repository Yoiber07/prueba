from django.db import models

# Create your models here.

class Servicios(models.Model):
    """
    docstring
    """

    idServicio = models.AutoField(primary_key=True)
    titulo = models.CharField( max_length=70,blank=False,null=False)
    descripcion = models.CharField(max_length=255,blank=False,null=False)
    # TODO: IMAGEN
    imagen = models.ImageField(upload_to='./static/image', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.titulo
    