# schedules/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('<int:id>/', views.schedule_detail, name='schedule_detail'),
    path('create/', views.schedule_create, name='schedule_create'),
    path('update/<int:id>/', views.schedule_update, name='schedule_update'),
    path('delete/<int:id>/', views.schedule_delete, name='schedule_delete'),
]
