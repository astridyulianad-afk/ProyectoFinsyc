from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreditoViewSet, AbonoCreditoViewSet, NotificacionesViewSet

router = DefaultRouter()
router.register('creditos', CreditoViewSet)
router.register('abonos', AbonoCreditoViewSet)
router.register('notificaciones', NotificacionesViewSet)

urlpatterns = [path('', include(router.urls))]
