from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, "login.html")

def registro(request):
    return render(request, "register.html")