# notifications/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notification
from .forms import NotificationForm

def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

def notification_detail(request, id):
    notification = get_object_or_404(Notification, id=id)
    return render(request, 'notifications/notification_detail.html', {'notification': notification})

def notification_create(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm()
    return render(request, 'notifications/notification_form.html', {'form': form})

def notification_update(request, id):
    notification = get_object_or_404(Notification, id=id)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('notification_list')
    else:
        form = NotificationForm(instance=notification)
    return render(request, 'notifications/notification_form.html', {'form': form})

def notification_delete(request, id):
    notification = get_object_or_404(Notification, id=id)
    if request.method == 'POST':
        notification.delete()
        return redirect('notification_list')
    return render(request, 'notifications/notification_confirm_delete.html', {'notification': notification})
