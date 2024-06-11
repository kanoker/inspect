# inspections/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inspection_list, name='inspection_list'),
    path('<int:id>/', views.inspection_detail, name='inspection_detail'),
    path('create/', views.inspection_create, name='inspection_create'),
    path('update/<int:id>/', views.inspection_update, name='inspection_update'),
    path('delete/<int:id>/', views.inspection_delete, name='inspection_delete'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicles/create/', views.vehicle_create, name='vehicle_create'),
    path('vehicles/<int:id>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicles/<int:id>/update/', views.vehicle_update, name='vehicle_update'),
    path('vehicles/<int:id>/delete/', views.vehicle_delete, name='vehicle_delete'),
]
