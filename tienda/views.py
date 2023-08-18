from django.shortcuts import render

# Create your views here.

def eco(request):
    contexto = {"usuario":"scubilla"}
    return render(request,'tienda/eco.html', contexto)

def alumnos(request):
    contexto = {
        "nombre":"Allegra",
        "apellido": "Cubilla",
        "edad": "46",
    }
    return render(request,'tienda/alumno.html', contexto)