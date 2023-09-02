from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

excValidator= FileExtensionValidator(['pdf'])

def validate_file_mimetype(file):
    accept=['application/pdf']
    fileMimeType = magic.from_buffer(file.read(1024), mime=True)
    print(fileMimeType)
    if fileMimeType not in accept:
        raise ValidationError("Unsupported file type")


# Create your models here.
class job(models.Model):
    client_name=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    description=models.TextField(blank=True, null=True)
    supervised_by=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    crew= models.TextField(blank=True, null=True)
    expected_Days_of_completion=models.PositiveIntegerField()
    actual_Days_of_completion=models.PositiveIntegerField(blank=True, null=True)
    survey_lithology=models.FileField(upload_to='media', validators=[excValidator, validate_file_mimetype])#llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
    drilling_plan=models.FileField(upload_to='media', validators=[excValidator, validate_file_mimetype])#kkkkkkkkkkkkkkkkkkkkkk
    casing_plan=models.FileField(blank=True, null=True, upload_to='media', validators=[excValidator, validate_file_mimetype])#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    start_date =models.DateField(blank=True, null=True)
    record_date= models.DateField(auto_now_add=True)