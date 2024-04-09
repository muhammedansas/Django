from django.contrib import admin
from .models import Departments, Doctors ,Products, Member
# Register your models here.



admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Products)
admin.site.register(Member)
