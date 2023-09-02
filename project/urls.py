
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('create-project/', views.createproject.as_view(), name='create-project'),
    path('list-project/', views.projectlist.as_view(), name='list-project'),
    path('project-details/<int:pk>', views.projectDetail.as_view(), name="project-detail"),
    path('update-project/<int:pk>', views.Updateproject.as_view(), name="update-project"),
    path('delete-project/<int:pk>', views.Deleteproject.as_view(), name="delete-project"),
]
