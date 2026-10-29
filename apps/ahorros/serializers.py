from rest_framework import serializers
from .models import Ahorro


class AhorroSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.ReadOnlyField(source='id_usuario.nombre')
    progreso = serializers.SerializerMethodField()
