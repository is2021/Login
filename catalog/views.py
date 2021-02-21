#welcome: Manejará la bienvenida al área para miembros y redireccionará a la vista de identificación si el usuario no ha iniciado la sesión.
#register: Manejará el formulario de registro de usuarios y autenticará al usuario automáticamente al registrarse.
#login: Manejará el formulario de identificación de usuarios y redireccionará a la portada si las credenciales son correctas.
#logout: Manejará la acción de cerrar la sesión y redirecciona a la vista de la portada de nuevo.
from django.shortcuts import render, redirect
