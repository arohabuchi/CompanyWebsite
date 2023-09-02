from django.db import models
from django.contrib.auth.models import User
# Create your models here.
status_choice = (
    ('New','Brand New'),
    ('Good','Good'),
    ('Untested','Untested'),
    ('Bad','Bad'),
    
)


class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    status = models.CharField(choices=status_choice, max_length=10)
    is_available = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    inventory_img = models.ImageField(upload_to="image/", blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name