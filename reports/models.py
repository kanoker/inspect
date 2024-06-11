# reports/models.py
from django.db import models
from inspections.models import Inspection

class Report(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    report_file = models.FileField(upload_to='reports/')
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('final', 'Final')])

    def __str__(self):
        return f"Report for {self.inspection} created on {self.created_at}"
