from django.shortcuts import render

def servicos_web(request):
    return render(request, 'servicos-web.html')

def servicos_marketing(request):
    return render(request, 'servicos-marketing.html')

def todos_os_servicos(request):
    return render(request, 'todos-os-servicos.html')

