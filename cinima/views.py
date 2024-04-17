from django.shortcuts import render, redirect
from . models import Movies

# Create your views here.
def home(request):
    movie_obj = Movies.objects.all()
    return render(request,'m_home.html',{"movie_obj":movie_obj})

def signup(request):
    return render(request,'m_signup.html')

def login(request):
    return render(request,'m_login.html')

def add(request):
    return render(request, 'm_add.html')

def adding(request):
    if request.POST:
        movie_name = request.POST['movie_name']
        movie_type = request.POST['movie_type']
        description = request.POST['description']
        image = request.POST['image']
        user = Movies(movie_name=movie_name,movie_type=movie_type,description=description,image=image)
        user.save()
        return redirect('m_home')

   