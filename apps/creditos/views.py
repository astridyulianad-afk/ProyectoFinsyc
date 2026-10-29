from rest_framework import viewsets
from .models import Credito, AbonoCredito, Notificaciones
from .serializers import CreditoSerializer, AbonoCreditoSerializer, NotificacionesSerializer

# Create your views here.
class CreditoViewSet(viewsets.ModelViewSet):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer

class AbonoCreditoViewSet(viewsets.ModelViewSet):
    queryset = AbonoCredito.objects.all()
    serializer_class = AbonoCreditoSerializer

class NotificacionesViewSet(viewsets.ModelViewSet):
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer