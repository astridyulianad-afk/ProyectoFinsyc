from django.contrib import admin

from .models import Credito, AbonoCredito, Notificaciones

admin.site.register(Credito)
admin.site.register(AbonoCredito)
admin.site.register(Notificaciones)
