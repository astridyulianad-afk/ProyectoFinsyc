from django.db import models

# Create your models here.

class Ahorro(models.Model):
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    meta = models.FloatField()
    monto_ahorrado = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_meta = models.DateField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.meta} - {self.monto_ahorrado}"