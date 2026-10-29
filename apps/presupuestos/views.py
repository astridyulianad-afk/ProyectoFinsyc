from rest_framework import viewsets
from .models import Presupuesto
from .serializers import PresupuestoSerializer

# Create your views here.
class PresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer