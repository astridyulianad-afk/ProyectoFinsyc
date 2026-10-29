from django.db import models

# Create your models here.
class Ingreso(models.Model):
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    monto = models.FloatField()
    fuente = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.fuente} - {self.monto}"