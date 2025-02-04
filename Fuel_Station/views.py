from django.shortcuts import render
from Fuel_Station import models as Fuel_Station_models
from Fuel_Station import serializers as Fuel_Station_serializers
from rest_framework import permissions
from rest_framework import generics

# Create your views here.

class FueltypeListCreate(generics.ListCreateAPIView):
    queryset = Fuel_Station_models.Fueltype.objects.all()
    serializer_class = Fuel_Station_serializers.FueltypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class FueltypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fuel_Station_models.Fueltype.objects.all()
    serializer_class = Fuel_Station_serializers.FueltypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class TankListCreate(generics.ListCreateAPIView):
    queryset = Fuel_Station_models.Tank.objects.all()
    serializer_class = Fuel_Station_serializers.TankSerializer
    permission_classes = [permissions.IsAuthenticated]

class TankRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fuel_Station_models.Tank.objects.all()
    serializer_class = Fuel_Station_serializers.TankSerializer
    permission_classes = [permissions.IsAuthenticated]


class DispenserListCreate(generics.ListCreateAPIView):
    queryset = Fuel_Station_models.Dispenser.objects.all()
    serializer_class = Fuel_Station_serializers.DispenserSerializer
    permission_classes = [permissions.IsAuthenticated]

class DispenserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fuel_Station_models.Dispenser.objects.all()
    serializer_class = Fuel_Station_serializers.DispenserSerializer
    permission_classes = [permissions.IsAuthenticated]

class NozzleListCreate(generics.ListCreateAPIView):
    queryset = Fuel_Station_models.Nozzle.objects.all()
    serializer_class = Fuel_Station_serializers.NozzleSerializer
    permission_classes = [permissions.IsAuthenticated]

class NozzleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fuel_Station_models.Nozzle.objects.all()
    serializer_class = Fuel_Station_serializers.NozzleSerializer
    permission_classes = [permissions.IsAuthenticated]
