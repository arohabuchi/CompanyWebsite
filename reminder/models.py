from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class reminder(models.Model):
    set_by=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    description= models.TextField()
    is_mail=models.BooleanField(default=False)
    date_of_action=models.DateField(blank=True, null=True)
    mail =models.EmailField(blank=True, null=True)
    date_set=models.DateField(auto_now_add=True)