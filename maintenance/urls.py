
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('create-maintenance/', views.createmaintenance.as_view(), name='create-maintenance'),
    path('list-maintenance/', views.maintenancelist.as_view(), name='list-maintenance'),
    path('maintenance-details/<int:pk>', views.maintenanceDetail.as_view(), name="maintenance-detail"),
    path('update-maintenance/<int:pk>', views.Updatemaintenance.as_view(), name="update-maintenance"),
    path('delete-maintenance/<int:pk>', views.Deletemaintenance.as_view(), name="delete-maintenance"),
]
