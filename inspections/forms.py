# inspections/forms.py
from django import forms
from .models import Inspection, Vehicle

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['vehicle', 'inspector', 'inspection_date', 'inspection_report', 'status']
        widgets = {
            'inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('pending', 'Pending'), ('completed', 'Completed')]),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['license_plate', 'make', 'model', 'year']

        