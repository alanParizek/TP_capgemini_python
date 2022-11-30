from django.shortcuts import render, redirect
# from django.forms import inlineformset_factory
from .forms import *


def inicio(request):
    form = LogInForm()
    context = {'form':form}
    return render(request, "login.html", context)

def registro(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, "register.html", context)