from django.db import models

# Create your models here.
class Credito(models.Model):
    id_usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    monto_total = models.FloatField()
    saldo_pendiente = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField()
    tasa_interes = models.FloatField()
    tipo_credito = models.CharField(max_length=100)
    entidad_financiera = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.saldo_pendiente} - {self.fecha_limite}"

class AbonoCredito(models.Model):
    id_credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    id_presupuesto = models.ForeignKey('presupuestos.Presupuesto', on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha_pago = models.DateField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.monto} - {self.id_credito}"

class Notificaciones(models.Model):
    id_credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=100)
    fecha_envio = models.DateField()
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.id_credito} - {self.mensaje}"