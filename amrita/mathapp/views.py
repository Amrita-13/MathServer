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
