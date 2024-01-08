from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required

#Signup Pagefrom django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.hashers import check_password

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

    #for showing the database data in frontend
    job = jobModel.objects.all()

    context = {
        'job':job
    }
    
    return render (request, 'viewjob.html',context)

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

#Delete job
def deletePage(request,myid):

    job = jobModel.objects.filter(id=myid)
    job.delete()

    return redirect ("viewjobPage")


#edit job
def editPage(request,myid):

    job = jobModel.objects.filter(id=myid)
    

    return render (request, "recruiter/editjob.html", {'job':job})

#Update job Page
def updatePage(request):

    user = request.user

    if request.method == "POST":
        job_id = request.POST.get('jobid')
        job_Title = request.POST.get('jobTitle')
        com_name = request.POST.get('companyName')
        location = request.POST.get('location')
        description = request.POST.get('description')
        job_Title = request.POST.get('jobTitle')

        job = jobModel(
            
            id = job_id,
            job_title = job_Title,
            company_name = com_name,
            location = location,
            description = description,
            job_creator = user,
        )

        job.save()

        return redirect("viewjobPage")
    

#Apply job
def applyPage(request,myid):

    job = jobModel.objects.filter(id=myid)

    return render (request,"jobseeker/applyjob.html")

#User Profile Page
def profilePage(request):

    return render (request,"profile.html")

#Edit User Profile Page
def editprofilePage(request):
    user = request.user

    if request.method == 'POST':
        userid = request.POST.get('user_id')
        username = request.POST.get('username')
        displayName = request.POST.get('displayName')
        email = request.POST.get('email')
        img = request.FILES.get('profilePic')
        mypass = request.POST.get('c_password')

        if not check_password(mypass, user.password):
            messages.error(request,"Wrong password given, profile is faild to update")
            return redirect("editprofilePage")
        
        user.id=userid
        user.username=username
        user.Display_name=displayName
        user.email=email
        
        if img:
            user.profile_picture=img

        user.save()
        messages.success(request,"Profile is successfully updated")
        return redirect("profilePage")

    return render (request,"editProfile.html")


#Change password Page
def changepasswordPage(request):

    user = request.user

    if request.method == 'POST':

        old_password=request.POST.get('currentPassword')
        newPassword=request.POST.get('newPassword')
        confirmPassword=request.POST.get('confirmPassword')

        if not check_password(old_password,user.password):
            messages.error(request,"Wrong password given")
            return redirect("changepasswordPage")
        
        if newPassword!=confirmPassword:
            messages.error(request,"New password and Confirm password is not matched")
            return redirect("changepasswordPage")
        
        else:
            user.set_password(confirmPassword)
            user.save()
            messages.success(request,"Password is successfully Changed")
            return redirect("loginPage")

    return render(request, "changepassword.html")
