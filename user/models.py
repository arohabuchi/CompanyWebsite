from django.db import models
from django.contrib.auth.models import User
from PIL import Image

position_choice = (
    ('staff','Staff'),
    ('Operation','Operation '),
    ('Accountant','Accountant'),
    ('HR','HR'),
    ('Admin','Admin'),
    
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(choices=position_choice, max_length=100, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)