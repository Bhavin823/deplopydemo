from django.shortcuts import render

# Create your views here.
def demopage(request):
    return render(request,'demoapp/demo.html')