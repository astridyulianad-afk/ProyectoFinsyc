from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    documento_identidad = models.CharField(max_length=20)
    correo = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombre