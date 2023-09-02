
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('create-job/', views.createjob.as_view(), name='create-job'),
    path('list-job/', views.joblist.as_view(), name='list-job'),
    path('job-details/<int:pk>', views.jobDetail.as_view(), name="job-detail"),
    path('update-job/<int:pk>', views.Updatejob.as_view(), name="update-job"),
    path('delete-job/<int:pk>', views.Deletejob.as_view(), name="delete-job"),
]
