# schedules/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule
from .forms import ScheduleForm

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedules/schedule_list.html', {'schedules': schedules})

def schedule_detail(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    return render(request, 'schedules/schedule_detail.html', {'schedule': schedule})

def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/schedule_form.html', {'form': form})

def schedule_update(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'schedules/schedule_form.html', {'form': form})

def schedule_delete(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'schedules/schedule_confirm_delete.html', {'schedule': schedule})
