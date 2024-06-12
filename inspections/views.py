# inspections/views.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Inspection, Vehicle, Photo
from .forms import InspectionForm, VehicleForm, PhotoForm


def inspection_list(request):
    inspections = Inspection.objects.all().order_by('-created_at')
    paginator = Paginator(inspections, 5)  # Show 5 inspections per page

    page_number = request.GET.get('page')
    try:
        # If page number is less than 1, raise EmptyPage
        page_number = int(page_number)
        if page_number < 1:
            raise EmptyPage
    except (TypeError, ValueError):
        # If page is not an integer, deliver first page.
        page_number = 1
    except EmptyPage:
        # If page is out of range (e.g., 9999 or less than 1), deliver last or first page of results.
        page_number = paginator.num_pages if page_number > paginator.num_pages else 1

    try:
        page_obj = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.page(1)

    return render(request, 'inspections/inspection_list.html', {'page_obj': page_obj, 'inspections': inspections})

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



def upload_photo(request, inspection_id):
    inspection = Inspection.objects.get(id=inspection_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.inspection = inspection
            form.save()
            return redirect('photo_list', inspection_id=inspection.id)
    else:
        form = PhotoForm(initial={'inspection': inspection})
    return render(request, 'inspections/upload_photo.html', {'form': form, 'inspection': inspection})

# def start_photo_session(request):
#     if request.method == 'POST':
#         form = PhotoSessionForm(request.POST)
#         if form.is_valid():
#             session = form.save()
#             return redirect('upload_photo')
#     else:
#         form = PhotoSessionForm()
#     return render(request, 'inspections/start_session.html', {'form': form})

# def start_inspection(request):
#     if request.method == 'POST':
#         form = InspectionForm(request.POST)
#         if form.is_valid():
#             inspection = form.save()
#             return redirect('start_session')
#     else:
#         form = InspectionForm()
#     return render(request, 'inspections/start_inspection.html', {'form': form})

def photo_list(request, inspection_id):
    inspection = Inspection.objects.get(id=inspection_id)
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'inspections/photo_list.html', {'inspection': inspection, 'photos': photos})

def photo_list_by_vehicle(request, vehicle_registration):
    vehicle = get_object_or_404(Vehicle, registration=vehicle_registration)
    inspections = Inspection.objects.filter(vehicle=vehicle)
    return render(request, 'inspection/photo_list_by_vehicle.html', {'vehicle': vehicle, 'inspections': inspections})


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'inspections/photo_detail.html', {'photo': photo})