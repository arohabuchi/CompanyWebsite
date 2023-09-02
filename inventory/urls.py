
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('create/', views.create.as_view(), name='create-inventory'),
    path('list/', views.inventorylist.as_view(), name='list-inventory'),
    path('inventory-details/<int:pk>', views.inventoryDetail.as_view(), name="inventory-detail"),
    path('update-inventory/<int:pk>', views.UpdateInventory.as_view(), name="update-inventory"),
    path('delete-inventory/<int:pk>', views.DeleteInventory.as_view(), name="delete-inventory"),
]
