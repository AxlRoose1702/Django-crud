from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #Con esta linea se crea un usuario
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                #Siempre el return para que no continue con el codigo siguiente
                return redirect('tarea')
            except IntegrityError:
                return HttpResponse('Usuario ya existe')
        return HttpResponse('contraseñas distintas')

def tarea(request):
    return render(request, 'tasks.html')

def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'inicioSesion.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'inicioSesion.html', {
                    'form': AuthenticationForm  ,
                    'error': 'usuario o contraseña incorrectos' 
            })


def cerrarSesion(request):
    logout(request)
    return redirect('inicio')