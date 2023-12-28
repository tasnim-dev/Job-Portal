from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.signupPage, name='signupPage'),
    path("dashboardPage", views.dashboardPage, name='dashboardPage'),
    
]
