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

def juguetes(request):
    dict_juguetes = {
        "juguete1":"pelota",
        "juguete2":"disco",
        "juguete3":"taca-taca",
    }
    return render(request,'tienda/juguetes.html', dict_juguetes)

def zapatos(request):
    dict_zapatos = {
        "zapato1":"mocasin",
        "zapato2":"bota",
        "zapato3":"punta fina",
    }
    return render(request,'tienda/zapatos.html', dict_zapatos)

def jardineria(request):
    dict_jardin = {
        "jardin1":"pelota",
        "jardin2":"disco",
        "jardin3":"taca-taca",
    }
    return render(request,'tienda/jardineria.html', dict_jardin)


def categoria(request):
    return render(request,'tienda/categorias.html')