from django.shortcuts import render

def fale_conosco(request):
    return render(request,'fale-conosco.html')

def localizacao(request):
    return render(request, 'localizacao.html')
