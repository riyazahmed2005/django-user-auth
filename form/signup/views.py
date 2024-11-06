from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth


# Create your views here.

def home(request):

    return render(request,'home.html')

def signup(request):

    if request.method=='POST':

        firstname=request.POST['Firstname']
        lastname=request.POST['Lastname']
        username=request.POST['Username']
        email=request.POST['Email']
        password=request.POST['pass']
        cpassword=request.POST['cpassword']

        if password==cpassword:

            if User.objects.filter(email=email).exists():
                
                return redirect('message', title="Info", message="Already registered !")
            else:

                user=User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request,"Registered successfully")
                return redirect('message', title="Success", message="Registered successfully")

        else:
            messages.error(request,"Password do not match")
            return redirect('message', title="error", message="Password not match")


    else:
        return render(request,'signup.html')

def login_user(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request,'login.html')

def message(request,title,message):
   
    return render(request,'message.html',{'title':title,'message':message})

def logout(request):
    auth.logout(request)
    return redirect('home')

