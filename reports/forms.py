# reports/forms.py
from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['inspection', 'report_file', 'status']
        widgets = {
          #  'created_at': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('draft', 'Draft'), ('final', 'Final')]),
        }
