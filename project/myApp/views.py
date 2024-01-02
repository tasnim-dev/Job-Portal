from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required

#Signup Pagefrom django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.contrib import messages

    # Handle the case where the username already exists
    # You can redirect the user to a different page or display an error message


# Create your views here.

#logout Page
def logoutPage(request):
    logout(request)
    return redirect('loginPage')



#login Page 
def loginPage(request):

    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')
        user = authenticate(request,username=user_name, password=user_pass)
        
        print(user)
        if user:
            login(request,user)
            return redirect("dashboardPage")

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
@login_required
def dashboardPage(request):

    return render(request, "dashboard.html")

#view job Page
def viewjobPage(request):
    
    return render (request, 'viewjob.html')

#Add job Page
def addjobPage(request):

    user = request.user

    if request.method == "POST":
        job_Title = request.POST.get('jobTitle')
        com_name = request.POST.get('companyName')
        location = request.POST.get('location')
        description = request.POST.get('description')
        job_Title = request.POST.get('jobTitle')

        job = jobModel(
            job_title = job_Title,
            company_name = com_name,
            location = location,
            description = description,
            job_creator = user,
        )

        job.save()

        return redirect("viewjobPage")


    return render (request, 'recruiter/addjob.html')