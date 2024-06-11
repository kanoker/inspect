# schedules/models.py
from django.db import models
from django.contrib.auth.models import User
from inspections.models import Vehicle

class Schedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed')])

    def __str__(self):
        return f"Schedule for {self.vehicle} on {self.scheduled_date}"
