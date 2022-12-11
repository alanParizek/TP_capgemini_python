from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Venta

# Create your views here.
class VentasController():
    @staff_member_required
    @staticmethod
    def verCaja(request):
        ventasPendientes = Venta.pendientesDePago()
        print(ventasPendientes)
        context = {'ventasPendientes':ventasPendientes}
        return render(request, 'caja.html', context)
    
    @staff_member_required
    @staticmethod
    def cobrar(request, idVenta):
        venta = Venta.objects.get(pk=idVenta)
        venta.cobrar()
        return redirect('ver_ventas')