from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
#importa template
from django.shortcuts import render
from django.template import RequestContext
#autenticar usuario
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
#forms
from .forms import registroForm

def index(request):
    return render(request,'index.html',{
        #context
        'message': 'listado de productos',
        'titulo': 'tienda',
        'products': [
            {'title':'playera','precio': 5,'stock': True}, #producto
            {'title':'camisa','precio': 12,'stock': True},
            {'title':'playera','precio': 1,'stock': False}
        ]
    })

def login_view(request):
        #login

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        """aunteticar"""

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Bienvenido {}'. format(user.username))
            return redirect('index')
        else:
            messages.error(request,'usuario o contraseña no validos')
    
    return render(request,'users/login.html',{
            
            #diccionario vacios
    })

def logout_view(request):
    """cierre de sesion"""
    logout(request)
    messages.success(request,'sesion cerrada exitosamente')
    return redirect('login')

def register(request):
    form = registroForm()
    return render (request,'users/registro.html', {
        'form': form

    })