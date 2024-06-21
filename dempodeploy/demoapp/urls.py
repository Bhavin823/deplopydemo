from django.urls import path
from demoapp import views
urlpatterns = [
    path('',views.demopage,name='demoapp'),

    path('addEmployee',views.addEmployee,name='addemp'),

    path('deletEmployee/<int:id>',views.deleteemployee,name='deleteemp')

]
