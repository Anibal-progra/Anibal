from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")
    
def nosotros(request):
    return render(request, "ProyectoWebApp/Nosotros.html")

def noticias(request):
    return render(request, "ProyectoWebApp/Noticias.html")

def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")

