from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, "home.html", {})

def desafio(request):
    empleados = [
    "Ana Martínez",
    "Luis Gómez",
    "Carlos Ramírez",
    "María Fernández",
    "Jorge Herrera",
    "Lucía Torres",
    "Diego López",
    "Elena Rivas",
    "Pedro Castillo",
    "Sofía Morales"
    ]
    return render(request, "desafio.html", {"empleados":empleados})