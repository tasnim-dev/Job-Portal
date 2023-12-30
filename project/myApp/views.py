from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

def loginPage(request):

    if request.method == "POST":
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')

        user = authenticate(request,username=user_name, password=user_pass)

        if user:
            login(request,user)
            return redirect('dashboardPage')

    return render (request, 'login.html')

#Signup Page
def signupPage(request):
    if request.method == "POST":

        uname=request.POST.get('username')
        d_name=request.POST.get('displayname')
        myemail=request.POST.get('email')
        mypass=request.POST.get('password')
        user_type=request.POST.get('userType')

        user = customUser.objects.create_user(username=uname,password=mypass)
        user.Display_name =d_name
        user.email=myemail
        user.user_type=user_type

        user.save()
        return render (request, 'register.html')



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
