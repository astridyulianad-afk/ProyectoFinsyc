from rest_framework import viewsets
from .models import MetodoPago, Gasto, SoportePago
from .serializers import MetodoPagoSerializer, GastoSerializer, SoportePagoSerializer

# Create your views here.
class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class SoportePagoViewSet(viewsets.ModelViewSet):
    queryset = SoportePago.objects.all()
    serializer_class = SoportePagoSerializer