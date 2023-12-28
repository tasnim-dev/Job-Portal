from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

def loginPage(request):
    return render (request, 'login.html')

#Signup Page
def signupPage(request):
    # if request.method == "POST":


    return render (request, 'register.html')

#Dashboard Page
def dashboardPage(request):
    user = request.user

    if user.is_authenticated:
        if user.user_type == 'recruiter':
            Template_name = 'recruiter/dashboard.html'
        
        elif user.user_type == 'jobseeker' :
            Template_name = 'jobseeker/dashboard.html'

        else:
            return HttpResponse ('invalid user')

    else:
        return HttpResponse('User is not authenticate')
    return render(request, Template_name)
