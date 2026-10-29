from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AhorroViewSet

router = DefaultRouter()
router.register('ahorros', AhorroViewSet)

urlpatterns = [path('', include(router.urls))]
