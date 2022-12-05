from django.shortcuts import render, redirect
# from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from carrito.models import Chango
from .forms import SignUpForm

from django.contrib.auth import authenticate, login, logout

def inicio(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('carrito')

    context = {}
    return render(request, "login.html", context)

def registro(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Chango.objects.create(usuario=usuario)
            return redirect('inicio')

    context = {'form':form}
    return render(request, "register.html", context)