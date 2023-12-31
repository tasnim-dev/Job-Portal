from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUser(AbstractUser):
    USER = [
        ('jobseeker','JobSeeker'),('recruiter','Recruiter')
    ]
    Display_name = models.CharField(max_length = 50,null=True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 50)
    confirm_password = models.CharField(max_length = 50,null=True)
    user_type = models.CharField(choices = USER,max_length = 50)

