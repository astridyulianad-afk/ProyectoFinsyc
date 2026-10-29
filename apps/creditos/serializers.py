from rest_framework import serializers
from .models import Credito, AbonoCredito, Notificaciones


class AbonoCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbonoCredito
        fields = '__all__'

class CreditoSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='id_usuario.nombre')

    class Meta:
        model = Credito
        fields = ['id', 'id_usuario', 'usuario_nombre', 'nombre', 'monto_total',
                'saldo_pendiente', 'fecha_inicio', 'fecha_limite',
                'tasa_interes', 'tipo_credito', 'entidad_financiera']

class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = '__all__'
