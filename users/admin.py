# users/admin.py
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone_number', 'address')

admin.site.register(UserProfile, UserProfileAdmin)
