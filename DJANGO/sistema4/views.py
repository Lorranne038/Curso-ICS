from django.shortcuts import render

def artigos_tecnologia(request):
    return render(request, 'artigos-tecnologia.html')

def artigos_saude(request):
    return render(request, 'artigos-saude.html')

def todos_os_artigos(request):
    return render(request, 'todos-os-artigos.html')
