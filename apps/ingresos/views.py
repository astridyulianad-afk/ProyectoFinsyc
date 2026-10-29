from rest_framework import viewsets
from .models import Ingreso
from .serializers import IngresoSerializer

# Create your views here.
class IngresoViewSet(viewsets.ModelViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer