from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def produto(request):
   
    return render(request, 'produto.html')


def sobre_loja(request):
    return render(request, 'sobre-a-loja.html')


def contato(request):
    return render(request, 'contato.html')