from django.contrib import admin
from inspections.models import Inspection, Vehicle


# Register your models here.
@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'inspector', 'inspection_date', 'inspection_report', 'status')
    list_filter = ('vehicle', 'inspector', 'inspection_date', 'status')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'make', 'model', 'year')
    list_filter = ('license_plate', 'make', 'model', 'year')
    






