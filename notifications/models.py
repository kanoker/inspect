# notifications/models.py
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sent_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('sent', 'Sent')])

    def __str__(self):
        return f"Notification to {self.recipient} on {self.sent_date}"
