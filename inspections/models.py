# inspections/models.py
from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.license_plate} - {self.make} {self.model} ({self.year})"

class Inspection(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    inspection_date = models.DateField()
    inspection_report = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])

    def __str__(self):
        return f"Inspection for {self.vehicle} on {self.inspection_date}"
