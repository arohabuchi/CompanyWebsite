
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('create-reminder/', views.createreminder.as_view(), name='create-reminder'),
    path('list-reminder/', views.reminderlist.as_view(), name='list-reminder'),
    path('reminder-details/<int:pk>', views.reminderDetail.as_view(), name="reminder-detail"),
    path('update-reminder/<int:pk>', views.Updatereminder.as_view(), name="update-reminder"),
    path('delete-reminder/<int:pk>', views.Deletereminder.as_view(), name="delete-reminder"),

]
