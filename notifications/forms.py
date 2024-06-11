# notifications/forms.py
from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['recipient', 'message', 'sent_date', 'status']
        widgets = {
            'sent_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('pending', 'Pending'), ('sent', 'Sent')]),
        }
