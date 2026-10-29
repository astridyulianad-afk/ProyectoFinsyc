from rest_framework import viewsets
from .models import Ahorro
from .serializers import AhorroSerializer

# Create your views here.
class AhorroViewSet(viewsets.ModelViewSet):
    queryset = Ahorro.objects.all()
    serializer_class = AhorroSerializer