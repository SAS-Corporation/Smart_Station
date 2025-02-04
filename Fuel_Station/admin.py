from django.contrib import admin
from Fuel_Station import models as Fuel_Station_models


# Register your models here.
admin.site.register(Fuel_Station_models.Fueltype)
admin.site.register(Fuel_Station_models.Tank)
admin.site.register(Fuel_Station_models.Dispenser)
admin.site.register(Fuel_Station_models.Nozzle)
