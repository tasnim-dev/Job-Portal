from django.contrib import admin
from .models import *

class customUser_view(admin.ModelAdmin):
    list_display = ['Display_name','email','user_type']

admin.site.register(customUser,customUser_view)
admin.site.register(jobModel)
admin.site.register(RecruiterProfile)
admin.site.register(JobSeekerProfile)