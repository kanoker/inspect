# inspections/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from datetime import datetime as dt
import os

def vehicle_image_path(instance, filename):
    # Extract the album name and current date
    inspection_id = str(instance.inspection.id)
    date_path = timezone.now().strftime('%Y-%m-%d')
    # Build the upload path
    return os.path.join('Photos', date_path, inspection_id, filename)

  
class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.license_plate} - {self.make} {self.model} ({self.year})"

class Inspection(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='inspections', on_delete=models.CASCADE)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    inspection_date = models.DateField()
    inspection_report = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inspection for {self.vehicle} on {self.inspection_date}"

# class PhotoSession(models.Model):
#     inspection = models.ForeignKey(Inspection, related_name='sessions', on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Session {self.id} for {self.inspection}"

class Photo(models.Model):
    # session = models.ForeignKey(PhotoSession, related_name='photos', on_delete=models.CASCADE, null=True)
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE, related_name='photos' , blank=True, null=True)
    image = models.ImageField(upload_to=vehicle_image_path)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 100)],
                                     format='JPEG',
                                     options={'quality': 60})
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.created_at} - {self.image} - {self.description[:20]} - {self.inspection}"
    