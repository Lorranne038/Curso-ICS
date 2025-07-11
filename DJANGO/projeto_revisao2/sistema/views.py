from django.shortcuts import render

def homepage(request):
    dados = {
        'titulo_pagina': 'Nossa amizade',
        'subtitulo_pagina':'A trajetoria da nossa amizade',
        'visitas': 123,
        'lista_visitas':[
            'Sarinha',
            'Gustavo',
            'Gregory',
            'Enzo',
            'Ana Ju',
            'Ana c.',
            'Dulci'
        ],
            'clientes': [
            {'nome': 'fulano', 'data_cadastro': '10/10/2010', 'saldo':100},
            {'nome': 'fulano', 'data_cadastro': '10/10/2010', 'saldo':100},
            {'nome':  'fulano', 'data_cadastro': '10/10/2010', 'saldo':100},
        ]
    }

    return render(request, 'index.html',dados)

def clientes(request):
    return render(request, 'cliente.html')

def produtos(request):
    return render(request, 'produtos.html')

def eletronicos(request):
    return render(request, 'produtos_eletronicos.html')

def contado_sobre(request):
    dados_empresa = {
        'titulo_pagina': '',
        'subtitulo_pagina':'',
        'contatos_empresa':'',
        'informacoes_sobre_empresa':' ',
    }
    return render(request, 'contatos_sobre.html',dados_empresa)


