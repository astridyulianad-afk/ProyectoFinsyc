from django.db import models

# Create your models here.
class PagosRecurrentes(models.Model):
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    id_metodo_pago = models.ForeignKey('gastos.MetodoPago', on_delete=models.CASCADE)
    id_soporte_factura = models.ForeignKey('gastos.SoportePago', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    monto = models.FloatField()
    frecuencia = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_proximo_pago = models.DateField()
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} - {self.monto} - {self.fecha_proximo_pago}"