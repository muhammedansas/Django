from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . forms import Dummy
from . models import Dummyitems

# Create your views here.

def signup(request):
    user=None
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

# /////////////////////////////  Forms //////////////////////////////////////////////

def mform(request):
    print(request)
    form = Dummy()
    if request.POST:
        form = Dummy(request.POST)
        if form.is_valid():
            
            form.save()
    dem = Dummyitems.objects.all()        
    return render(request, 'Forms/model_form.html',{"frm":form,"dem":dem})

# ////////////////////////////////////////////////////////////////////////////////////////