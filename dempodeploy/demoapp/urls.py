from django.urls import path
from demoapp import views
urlpatterns = [
    path('',views.demopage,name='demoapp'),
]
