from django.shortcuts import render, redirect
# from django.forms import inlineformset_factory
from .forms import *

from django.contrib.auth import authenticate, login, logout


def inicio(request):
    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('password')

    context = {}
    return render(request, "login.html", context)

def registro(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('inicio')


    context = {'form':form}
    return render(request, "register.html", context)