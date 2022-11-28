from django.shortcuts import render
from .forms import *

# Create your views here.
def carrito(request):
    formCarrito = CarritoForm()
    context = {'form':formCarrito}
    return render(request, "carrito.html") #, context)
    
    