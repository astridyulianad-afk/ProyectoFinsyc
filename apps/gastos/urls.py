from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MetodoPagoViewSet, GastoViewSet, SoportePagoViewSet

router = DefaultRouter()
router.register('metodos-pago', MetodoPagoViewSet)
router.register('gastos', GastoViewSet)
router.register('soportes-pago', SoportePagoViewSet)

urlpatterns = [path('', include(router.urls))]
