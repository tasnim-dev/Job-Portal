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


class jobModel(models.Model):
    job_title=models.CharField(max_length=100, null=True)
    company_name=models.CharField(max_length=100, null=True)
    location=models.CharField(max_length=100, null=True)
    description=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True, null=True)
    job_creator=models.ForeignKey(customUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title
    
#Recruiter Profile
class RecruiterProfile(models.Model):
    user = models.OneToOneField(customUser, on_delete=models.CASCADE, related_name='recruiterProfile')
    profile_picture=models.ImageField(upload_to="media/profile_pic", null=True)

    def __str__(self):
        return self.user.Display_name

#JobSeeker Profile   
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(customUser, on_delete=models.CASCADE, related_name='jobseekerProfile')
    profile_picture=models.ImageField(upload_to="media/profile_pic", null=True)

    def __str__(self):
        return self.user.Display_name