from rest_framework import serializers
from .models import Ingreso


class IngresoSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='id_usuario.nombre')

    class Meta:
        model = Ingreso
        fields = ['id', 'id_usuario', 'usuario_nombre', 'monto', 'fuente',
                  'descripcion', 'fecha_ingreso']

