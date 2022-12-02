from django.shortcuts import render
from .forms import *


def inicio(request):
    form = LogInForm()
    context = {'form':form}
    return render(request, "login.html", context)

def registro(request):
    form = SignUpForm()
    context = {'form':form}
    return render(request, "register.html", context)