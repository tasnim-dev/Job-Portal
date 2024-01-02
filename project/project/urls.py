from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.signupPage, name='signupPage'),
    path("loginPage", views.loginPage, name='loginPage'),
    path("logoutPage", views.logoutPage, name="logoutPage"),
    path("dashboardPage",views.dashboardPage, name='dashboardPage'),
    path("viewjobPage", views.viewjobPage, name='viewjobPage'),
    path("addjobPage", views.addjobPage, name='addjobPage'),
    
]
