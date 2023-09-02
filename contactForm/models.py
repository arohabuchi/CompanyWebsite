from django.db import models

# Create your models here.
class contactForm(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    datePosted = models.DateField(auto_now_add=True)