# schedules/forms.py
from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['vehicle', 'inspector', 'scheduled_date', 'status']
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('scheduled', 'Scheduled'), ('completed', 'Completed')]),
        }
