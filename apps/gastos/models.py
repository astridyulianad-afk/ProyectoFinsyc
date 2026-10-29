from django.db import models

# Create your models here.
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    nota = models.CharField(max_length=100)
    precio = models.FloatField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.precio}"

class SoportePago(models.Model):
    id_gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    nombre_archivo = models.CharField(max_length=100)
    ruta_archivo = models.CharField(max_length=100)
    tipo_archivo = models.CharField(max_length=100)
    fecha_subida = models.DateField()

    def __str__(self):
        return self.nombre_archivo