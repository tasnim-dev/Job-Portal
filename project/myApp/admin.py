from django.contrib import admin
from .models import customUser

class customUser_view(admin.ModelAdmin):
    list_display = ['Display_name','email','user_type']

admin.site.register(customUser,customUser_view)