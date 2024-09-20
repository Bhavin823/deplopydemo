from django.contrib import admin
from demoapp.models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','age','image']

admin.site.register(Employee,EmployeeAdmin)
