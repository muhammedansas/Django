from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Departments, Doctors, Products, Member

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

def crud(request):
    dict_member = {
        "member" : Member.objects.all()
    }
    return render(request, 'crud_home.html',dict_member)

def crud_add(request):
    return render(request, 'crud_add.html')

def addrec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    mem = Member(first_name = x, last_name = y, country = z)
    mem.save()
    return redirect('/crud')

def delete(request,id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect('/crud')

def update(request,id):
    mem = Member.objects.get(id = id)
    return render(request, 'crud_update.html',{"mem":mem})

def uprec(request,id):
    x = request.POST['first']   
    y = request.POST['last']
    z = request.POST['country']
    mem = Member.objects.get(id = id)
    mem.first_name = x
    mem.last_name = y
    mem.country = z
    mem.save()
    return redirect('/crud')

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

# class based view (cbv) examples:

class Myview(View):
    def get(self,request):
        return HttpResponse('get request handled')
    
    def post(self,request):
        return HttpResponse()