from rest_framework import serializers
from Fuel_Station import models as Fuel_Station_models


class FueltypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fuel_Station_models.Fueltype
        fields = '__all__'


class TankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fuel_Station_models.Tank
        fields = '__all__'

class DispenserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fuel_Station_models.Dispenser
        fields = '__all__'


class NozzleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fuel_Station_models.Nozzle
        fields = '__all__'


