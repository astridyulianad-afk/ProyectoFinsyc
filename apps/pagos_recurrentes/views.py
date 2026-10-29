from rest_framework import viewsets
from .models import PagosRecurrentes
from .serializers import PagosRecurrentesSerializer

# Create your views here.
class PagosRecurrentesViewSet(viewsets.ModelViewSet):
    queryset = PagosRecurrentes.objects.all()
    serializer_class = PagosRecurrentesSerializer