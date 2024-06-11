# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('<int:id>/', views.report_detail, name='report_detail'),
    path('create/', views.report_create, name='report_create'),
    path('update/<int:id>/', views.report_update, name='report_update'),
    path('delete/<int:id>/', views.report_delete, name='report_delete'),
]
