from django.db import models

# Create your models here.
class project(models.Model):
    project_image = models.ImageField(upload_to='image')
    location=models.CharField(max_length=100)
    description=models.CharField(max_length=250, blank=True, null=True)