# users/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('inspector', 'Inspector'),
        ('insurance_agent', 'Insurance Agent'),
        ('customer', 'Customer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_inspector(self):
        return self.role == 'inspector'

    @property
    def is_insurance_agent(self):
        return self.role == 'insurance_agent'

    @property
    def is_customer(self):
        return self.role == 'customer'
