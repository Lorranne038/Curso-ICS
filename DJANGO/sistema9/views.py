from django.shortcuts import render

def eventos_futuros(request):
    return render(request,'eventos-futuros.html')

def eventos_passados(request):
    return render(request,'eventos-passados.html')

def todos_os_eventos(request):
    return render(request,'todos-os-eventos.html')