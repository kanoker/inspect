# inspections/urls.py
from django.conf import settings
from django.conf.urls.static import static
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
    path('<int:inspection_id>/upload/', views.upload_photo, name='upload_photo'),
    # path('start_session/', views.start_photo_session, name='start_session'),
    # path('start_inspection/', views.start_inspection, name='start_inspection'),
    path('photos/<int:inspection_id>/', views.photo_list, name='photo_list'),
    path('photos/vehicle/<str:vehicle_license_plate>/', views.photo_list_by_vehicle, name='photo_list_by_vehicle'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
