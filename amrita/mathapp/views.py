from django.shortcuts import render 

def bmi_calculator(request): 
    context = {} 
    context['bmi'] = "0" 
    context['w'] = "0" 
    context['h'] = "0" 
    
    if request.method == 'POST': 
        print("POST method is used")
        
        w = request.POST.get('weight', '0')
        h = request.POST.get('height', '0')
        
        print('request=', request) 
        print('Weight=', w) 
        print('Height=', h) 
       
        try:
            weight = float(w)
            height = float(h)
            bmi = weight / (height ** 2)
        except ZeroDivisionError:
            bmi = "Invalid height (cannot be zero)"
        except ValueError:
            bmi = "Invalid input (enter numeric values)"
        
        context['bmi'] = bmi 
        context['w'] = w
        context['h'] = h 
        print('BMI=', bmi) 
    
    return render(request, 'mathapp/math.html', context)