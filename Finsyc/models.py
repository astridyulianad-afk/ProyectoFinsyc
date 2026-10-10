

from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField( max_length=100)
    documento_identidad = models.CharField(max_length=20)
    correo = models.EmailField(max_length=200)
    def __str__(self):
        return self.nombre
class Ingreso(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.FloatField()
    fuente = models.CharField( max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    def __str__(self):
        return f"{self.fuente} - {self.monto}"
    
class Presupuesto(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    descripcion = models.CharField(max_length=100)
    monto_actual =  models.FloatField()
    fecha_inicio = models.DateField()
    def __str__(self):
        return f"{self.monto_actual} - {self.descripcion}"

class Ahorro(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    meta = models.FloatField()
    monto_ahorrado = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_meta = models.DateField()
    descripcion =  models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.meta} - {self.monto_ahorro}"

class MetodoPago(models.Model):
    nombre =  models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
        
class Gasto(models.Model):
    id_usuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    nota = models.CharField(max_length=100)
    precio = models.FloatField()
    fecha = models.DateField()
    def __str__(self):
        return  f"{self.nombre} - {self.precio}"

class SoportePago(models.Model):
    id_gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    nombre_archivo = models.CharField(max_length=100)
    ruta_archivo = models.CharField(max_length=100)
    tipo_archivo = models.CharField(max_length=100)
    fecha_subida = models.DateField()
    def __str__(self):
        return self.nombre_archivo

class Credito(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    monto_total = models.FloatField()
    saldo_pendiente = models.FloatField()
    fecha_inicio  = models.DateField()
    fecha_limite =  models.DateField()
    tasa_interes = models.FloatField()
    tipo_credito = models.CharField(max_length=100)
    entidad_financiera = models.CharField(max_length=100)
    
    def __str__(self):
        return  f"{self.nombre} - {self.saldo_pendiente} - {self.fecha_limite}"
    
class AbonoCredito(models.Model):
    id_credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    id_presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha_pago  =  models.DateField()
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return  f"{self.monto} - {self.id_credito}"

class PagosRecurrentes(models.Model):  
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    id_soporte_factura = models.ForeignKey(SoportePago, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    monto = models.FloatField()
    frecuencia = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_proximo_pago = models.DateField()
    estado = models.BooleanField()
    
    def __str__(self):
            return  f"{self.nombre} - {self.monto} - {self.fecha_proximo_pago}" 
        
class Notificaciones(models.Model):
    id_credito =models.ForeignKey(Credito, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=100)
    fecha_envio = models.DateField()
    estado = models.BooleanField()
    def __str__(self):
        return  f"{self.id_credito} - {self.mensaje} " 
            