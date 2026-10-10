from django.contrib import admin
from .models import Usuario, Gasto, Ingreso, Presupuesto, Ahorro, AbonoCredito, MetodoPago, Credito, PagosRecurrentes, Notificaciones, SoportePago

admin.site.register(Usuario)
admin.site.register(Gasto)
admin.site.register(Ingreso)
admin.site.register(Presupuesto)
admin.site.register(Ahorro)
admin.site.register(AbonoCredito)
admin.site.register(MetodoPago)
admin.site.register(Notificaciones)
admin.site.register(Credito)
admin.site.register(PagosRecurrentes)
admin.site.register(SoportePago)