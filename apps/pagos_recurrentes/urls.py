from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PagosRecurrentesViewSet

router = DefaultRouter()
router.register('pagos-recurrentes', PagosRecurrentesViewSet)

urlpatterns = [path('', include(router.urls))]
