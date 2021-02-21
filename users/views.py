#welcome: Manejará la bienvenida al área para miembros y redireccionará a la vista de identificación si el usuario no ha iniciado la sesión.
#register: Manejará el formulario de registro de usuarios y autenticará al usuario automáticamente al registrarse.
#login: Manejará el formulario de identificación de usuarios y redireccionará a la portada si las credenciales son correctas.
#logout: Manejará la acción de cerrar la sesión y redirecciona a la vista de la portada de nuevo.
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm

def welcome(request):
    return render(request, "users/welcome.html")

def register(request):
    return render(request, "users/register.html")

def login(request):
    return render(request, "users/login.html")

def logout(request):
    # Redireccionamos a la portada
    return redirect('/')

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "users/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})