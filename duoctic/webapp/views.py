from django.shortcuts import render


# Create your views here.

def plantilla(request):
    return render(request, 'templates/plantilla.html', {})

def index(request):
    return render(request, 'index.html', {})

def docentes(request):
    return render(request, 'docentes.html', {})

def estudiantes(request):
    return render(request, 'estudiantes.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})




