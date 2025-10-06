from django.contrib import admin 
from django.urls import path 
from mathapp import views 

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('bmicalculator/', views.bmi_calculator, name="bmicalculator"),
    path('', views.bmi_calculator, name="bmicalculatorroot")
]