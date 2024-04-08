from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Departments, Doctors, Products

# Create your views here.

def index(request):
    perosns = {
        "name":"ansas",
        "age":10,
        "place" : "olavanna"
    }
    return render(request, 'index.html',perosns)

def home(request):
    return HttpResponse("home page")

def contact(request):
    return render(request, 'Contact.html')

def about(request):
    return render(request, "About.html")

def session(request):
    return render(request, "session.html")

def department(request):
    dict_dept = {
        "dept" : Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)

def doctors(request):
    dict_docs = {
        "doctors" : Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)

def products(request):
    dict_prdct = {
        "prdcts" : Products.objects.all()
    }
    return render(request, 'products.html',dict_prdct)