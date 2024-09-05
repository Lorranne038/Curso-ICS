from django.shortcuts import render

def galeria_natureza(request):
    return render(request, 'galeria-natureza.html')

def galeria_urbanas(request):
    return render(request, 'galeria-urbanas.html')


