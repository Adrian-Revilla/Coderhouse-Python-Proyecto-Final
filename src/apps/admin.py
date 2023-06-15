from django.contrib import admin
from . import models

admin.site.register(models.Conductor)
admin.site.register(models.Viaje)
admin.site.register(models.Vehiculo)