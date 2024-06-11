# inspections/views.py
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Inspection, Vehicle
from .forms import InspectionForm, VehicleForm

def inspection_list(request):
    inspections = Inspection.objects.all()
    return render(request, 'inspections/inspection_list.html', {'inspections': inspections})

def inspection_detail(request, id):
    inspection = get_object_or_404(Inspection, id=id)
    return render(request, 'inspections/inspection_detail.html', {'inspection': inspection})

def inspection_create(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inspection_list')
    else:
        form = InspectionForm()
    return render(request, 'inspections/inspection_form.html', {'form': form})

def inspection_update(request, id):
    inspection = get_object_or_404(Inspection, id=id)
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES, instance=inspection)
        if form.is_valid():
            form.save()
            return redirect('inspection_list')
    else:
        form = InspectionForm(instance=inspection)
    return render(request, 'inspections/inspection_form.html', {'form': form})

def inspection_delete(request, id):
    inspection = get_object_or_404(Inspection, id=id)
    if request.method == 'POST':
        inspection.delete()
        return redirect('inspection_list')
    return render(request, 'inspections/inspection_confirm_delete.html', {'inspection': inspection})


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'inspections/vehicle_list.html', {'vehicles': vehicles})

def vehicle_detail(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    return render(request, 'inspections/vehicle_detail.html', {'vehicle': vehicle})

def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'inspections/vehicle_form.html', {'form': form})

def vehicle_update(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'inspections/vehicle_form.html', {'form': form})

def vehicle_delete(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'inspections/vehicle_confirm_delete.html', {'vehicle': vehicle})


def index(request):
    context = {}
    return render(request,"index.html",context)


def aboutus(request):
    context = {}
    return render(request,"about-us.html",context)