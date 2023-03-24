from django.http import HttpResponse

def suma(request, num1, num2):
    resultado = int(num1) + int(num2)
    return HttpResponse("La suma de {} y {} es {}".format(num1, num2, resultado))

def resta(request, num1, num2):
    resultado = int(num1) - int(num2)
    return HttpResponse("La resta de {} y {} es {}".format(num1, num2, resultado))

def multiplicacion(request, num1, num2):
    resultado = int(num1) * int(num2)
    return HttpResponse("La multiplicacion de {} y {} es {}".format(num1, num2, resultado))

