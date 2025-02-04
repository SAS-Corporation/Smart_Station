from django.db import models

# Create your models here.


class Fueltype(models.Model):
    name = models.CharField(max_length=50)
    price_per_unit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tank(models.Model):
    name = models.CharField(max_length=50)
    fueltype = models.ForeignKey(Fueltype, on_delete=models.CASCADE)
    capacity = models.FloatField()
    current_volume = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.fueltype.name}"

class Dispenser(models.Model):
    name = models.CharField(max_length=50)
    tank = models.ManyToManyField(Tank)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return f"{self.name} - {self.tank.all().first().name if self.tank.all().exists() else 'No Tank'}"
    
class Nozzle(models.Model):
    name = models.CharField(max_length=50)
    dispenser = models.ForeignKey(Dispenser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return f"{self.name} - {self.dispenser.name}"