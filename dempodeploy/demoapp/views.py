from django.shortcuts import render,redirect
from demoapp.models import Employee
# Create your views here.
def demopage(request):
    employes = Employee.objects.all()
    
    context = {
        'employee':employes,
    }
    return render(request,'demoapp/demo.html',context)

def addEmployee(request):
    if request.method == "POST":
        employee = Employee()
        employee.name = request.POST.get('name')
        employee.age = request.POST.get('age')

        if request.FILES != 0:
            employee.image = request.FILES.get('image')
        
        employee.save()
    
    return redirect('demoapp')

def deleteemployee(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('demoapp')