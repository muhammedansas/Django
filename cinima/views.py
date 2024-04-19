from django.shortcuts import render, redirect
from . models import Movies
from . forms import Fmovie

# Create your views here.
def home(request):
    movie_obj = Movies.objects.all()
    return render(request,'m_home.html',{"movie_obj":movie_obj})

def signup(request):
    return render(request,'m_signup.html')

def login(request):
    return render(request,'m_login.html')

def add(request):
    form = Fmovie()
    if request.POST:
        form = Fmovie(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'm_add.html',{'form':form})

def adding(request):
    if request.POST:
        movie_name = request.POST['movie_name']
        movie_type = request.POST['movie_type']
        description = request.POST['description']
        movie_image = request.POST['movie_image']
        user = Movies(movie_name=movie_name,movie_type=movie_type,description=description,movie_image=movie_image)
        user.save()
        return redirect('m_home')
    
def delete(request,id):
    movie = Movies.objects.get(id=id)
    movie.delete()
    return redirect('m_home') 

def update(request,id):
    movie = Movies.objects.get(id=id)
    fmovie = Fmovie(instance=movie)
    if request.POST:
        fmovie = Fmovie(request.POST)
        if fmovie.is_valid():
            fmovie.save()
    return render(request,'m_update.html',{"movie":movie,"fmovie":fmovie})

def update(request,id):
    movie_name = request.POST["movie_name"]
    movie_type = request.POST['movie_type']
    description = request.POST["description"]
    movie_image = request.POST["movie_image"]
    movie = Movies.objects.get(id = id)
    movie.movie_name = movie_name
    movie.movie_type = movie_type
    movie.description = description
    movie.movie_image = movie_image
    movie.save()
    return redirect('/m_home')


   