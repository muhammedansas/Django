from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Departments, Doctors, Products, Member
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    perosns = {
        "name":"ansas",
        "age":10,
        "place" : "olavanna"
    }
    return render(request, 'index.html',perosns)

@login_required(login_url='login')
def home(request):
    return HttpResponse("home page")

@login_required(login_url='login')
def contact(request):
    return render(request, 'Contact.html')

@login_required(login_url='login')
def about(request):
    return render(request, "About.html")

@login_required(login_url='login')
def session(request):
    return render(request, "session.html")

                                # CRUD
# //////////////////////////////////////////////////////////////////////////

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

# //////////////////////////////////////////////////////////////////////
@login_required(login_url='login')
def department(request):
    dict_dept = {
        "dept" : Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)


@login_required(login_url='login')
def doctors(request):
    dict_docs = {
        "doctors" : Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)


@login_required(login_url='login')
def products(request):
    print(request.COOKIES)
    visits=int(request.COOKIES.get('count',0))     # request.COOKIES['count'] = '0'    this is happening here
    visits = visits+1
    responce = render(request, 'products.html',{'prdcts':Products.objects.all(),'visits':visits})
    responce.set_cookie('count',visits)
    return responce

