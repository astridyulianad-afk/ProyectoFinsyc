from rest_framework import serializers
from .models import PagosRecurrentes


class PagosRecurrentesSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='id_usuario.nombre')
    metodo_pago_nombre = serializers.ReadOnlyField(source='id_metodo_pago.nombre')

    class Meta:
        model = PagosRecurrentes
        fields = ['id', 'id_usuario', 'usuario_nombre', 'id_metodo_pago',
                'metodo_pago_nombre', 'id_soporte_factura', 'nombre', 'monto',
                'frecuencia', 'fecha_inicio', 'fecha_proximo_pago', 'estado']
