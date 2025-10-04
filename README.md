# Ex.05 Design a Website for Server Side Processing
## Date:30.09.2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>
<head>
<style>
body{
    background-color:black;
}
.formelt{
    color:orange;
    text-align: center;
    margin-top: 7px;
    margin-bottom: 6px;
}
h1{
    color:darkred;
    text-align: center;
    padding-top: 20px;
}
</style>
</head>
<body>
    <h1 style="color:antiquewhite" align="center">Amrita B.S(25018474)</h1>
<div class="edge">
<div class="box">
<h1>Power Calculation (P = I × R²)</h1>
<form method="POST">
    {% csrf_token %}
    <div class="formelt">
        Current (I): <input type="text" name="current" value="{{I}}">(in Amperes)<br/>
    </div>
    <div class="formelt">
        Resistance (R): <input type="text" name="resistance" value="{{R}}">(in Ohms)<br/>
    </div>
    <div class="formelt">
        <input type="submit" value="Calculate"><br/>
    </div>
    <div class="formelt">
        Power (P): <input type="text" name="power" value="{{power}}">(in Watts)<br/>
    </div>
</form>
</div>
</div>
</body>
</html>

views.py
from django.shortcuts import render

def powercalc(request):
    context = {}
    context['power'] = "0"
    context['I'] = "0"
    context['R'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        I = request.POST.get('current', '0')
        R = request.POST.get('resistance', '0')

        print('Current (I) =', I)
        print('Resistance (R) =', R)
        power = int(I) * (int(R) ** 2)

        context['power'] = power
        context['I'] = I
        context['R'] = R

        print('Power (P) =', power)

    return render(request, 'mathapp/math.html', context)

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('power/', views.powercalc, name="powercalc"),
    path('', views.powercalc, name="powercalcroot"),  
]

```

## SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-10-04 080437.png>)
## HOMEPAGE:
![alt text](<Screenshot 2025-10-01 185649.png>)

## RESULT:
The program for performing server side processing is completed successfully.
