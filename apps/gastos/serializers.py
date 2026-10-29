from rest_framework import serializers
from .models import MetodoPago, Gasto, SoportePago


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'


class SoportePagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoportePago
        fields = '__all__'


class SoporteResumenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoportePago
        fields = ['id', 'nombre_archivo', 'tipo_archivo', 'fecha_subida']


class GastoSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='id_usuario.nombre')
    metodo_pago_nombre = serializers.ReadOnlyField(source='id_metodo_pago.nombre')
    soportes = SoporteResumenSerializer(source='soportepago_set', many=True, read_only=True)

    class Meta:
        model = Gasto
        fields = ['id', 'id_usuario', 'usuario_nombre', 'id_metodo_pago',
                'metodo_pago_nombre', 'nombre', 'nota', 'precio', 'fecha', 'soportes']
