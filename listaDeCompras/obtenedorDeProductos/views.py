from django.shortcuts import render
from django.http import HttpResponse
from obtenedorDeProductos.models import obtenedorDeProductos

# Create your views here.

def funcion(request):
    op = obtenedorDeProductos()
    return HttpResponse(op.todosLosProductos)
