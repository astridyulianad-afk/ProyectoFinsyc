from rest_framework import serializers
from .models import Presupuesto


class PresupuestoSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='id_usuario.nombre')

    class Meta:
        model = Presupuesto
        fields = ['id', 'id_usuario', 'usuario_nombre', 'descripcion',
                  'monto_actual', 'fecha_inicio']
