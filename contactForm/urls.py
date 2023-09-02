
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('create-contactForm/', views.createcontactForm.as_view(), name='create-contactForm'),
    path('list-contactForm/', views.contactFormlist.as_view(), name='list-contactForm'),
    path('delete-contactForm/<int:pk>', views.DeletecontactForm.as_view(), name="delete-contactForm"),
]
