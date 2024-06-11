# reports/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Report
from .forms import ReportForm

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

def report_detail(request, id):
    report = get_object_or_404(Report, id=id)
    return render(request, 'reports/report_detail.html', {'report': report})

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

def report_update(request, id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'reports/report_form.html', {'form': form})

def report_delete(request, id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'reports/report_confirm_delete.html', {'report': report})
