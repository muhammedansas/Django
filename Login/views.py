from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup(request):
    
    error_message=None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message = str(e)    
        print(username,password)
    return render(request, 'Login_templates/signup.html', {"user":user,'error_message':error_message})

def user_login(request):
    error_message=None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message = "invalid"    

    return render(request, 'Login_templates/login.html',{'error_message':error_message})

def user_logout(request):
    logout(request)
    return redirect('login')