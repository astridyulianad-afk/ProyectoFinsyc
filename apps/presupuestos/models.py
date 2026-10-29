from django.db import models

# Create your models here.
class Presupuesto(models.Model):
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    monto_actual = models.FloatField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return f"{self.monto_actual} - {self.descripcion}"