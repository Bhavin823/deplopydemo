from django.contrib import admin
from demoapp.models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','age']

admin.site.register(Employee,EmployeeAdmin)
