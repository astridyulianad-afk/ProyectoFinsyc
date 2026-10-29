from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PresupuestoViewSet

router = DefaultRouter()
router.register('presupuestos', PresupuestoViewSet)

urlpatterns = [path('', include(router.urls))]
