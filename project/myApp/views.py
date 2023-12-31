from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
#Signup Pagefrom django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.contrib import messages

    # Handle the case where the username already exists
    # You can redirect the user to a different page or display an error message


# Create your views here.

def loginPage(request):

    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')
        user = authenticate(request,username=user_name, password=user_pass)
        
        print(user)
        if user:
            login(request,user)
            return HttpResponse("Login Successfully")

    return render (request, 'login.html')

def signupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        d_name = request.POST.get('displayName')
        myemail = request.POST.get('email')
        mypass = request.POST.get('password')
        user_type = request.POST.get('userType')

        try:
            user = get_user_model().objects.create_user(username=uname, email=myemail, password=mypass)
        except IntegrityError:
            # Handle the case where the username already exists
            # You can redirect the user to a different page or display an error message
            
            messages.warning(request,'Username already exists. Please choose a different username')
            return render(request, 'signup.html')

        user.Display_name = d_name
        user.email = myemail
        user.user_type = user_type

        user.save()
        return redirect('loginPage')

    return render(request, 'signup.html')


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
