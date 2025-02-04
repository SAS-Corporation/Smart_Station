from django.urls import path
from Fuel_Station import views as Fuel_Station_views


urlpatterns = [
    
    # Fueltype URLs
    path('fueltypes/', Fuel_Station_views.FueltypeListCreate.as_view(), name='fueltype-list-create'),
    path('fueltypes/<int:pk>/', Fuel_Station_views.FueltypeRetrieveUpdateDestroy.as_view(), name='fueltype-retrieve-update-delete'),

    # Tank URLs
    path('tanks/', Fuel_Station_views.TankListCreate.as_view(), name='tank-list-create'),
    path('tanks/<int:pk>/', Fuel_Station_views.TankRetrieveUpdateDestroy.as_view(), name='tank-retrieve-update-delete'),

    # Dispenser URLs
    path('dispensers/', Fuel_Station_views.DispenserListCreate.as_view(), name='dispenser-list-create'),
    path('dispensers/<int:pk>/', Fuel_Station_views.DispenserRetrieveUpdateDestroy.as_view(), name='dispenser-retrieve-update-delete'),

    # Nozzle URLs
    path('nozzles/', Fuel_Station_views.NozzleListCreate.as_view(), name='nozzle-list-create'),
    path('nozzles/<int:pk>/', Fuel_Station_views.NozzleRetrieveUpdateDestroy.as_view(), name='nozzle-retrieve-update-delete'),

]