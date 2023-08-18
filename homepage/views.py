from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mostrar(request):
    return HttpResponse('pagina de prueba')

