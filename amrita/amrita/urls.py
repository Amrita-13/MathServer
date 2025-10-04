from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('power/', views.powercalc, name="powercalc"),
    path('', views.powercalc, name="powercalcroot"),  
]
