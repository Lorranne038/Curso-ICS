from django.shortcuts import render

def homepage(request):
    dados = {
        'titulo_pagina':'Contato da Empresa',  
        'Telefone':' (11) 1234-5678',
        'E-mail': 'contato@empresa.com.br',
        'Endereço': 'Rua Av.Industrias, 123, Bairro , Buritizeiro - mg, CEP 12345-678',
        'Site': 'www.institutocafesolidario.org.br/',
        'Redes Sociais': '-Facebook: facebook.com/ics- Instagram: instagram.com/ics- LinkedIn: linkedin.com/company/ics',
        'titulo2_pagina':'Sobre Contato',
        'nome_empresa':'nome completo da empresa',
        'endereco':'Localização Física',
        'contatos_telefonicos':'Telefone Principal, Telefones Alternativos',
        'horario_atendimento':'Dia e Hora em que a empresa está disponivel',
        'formulario_contato':'Um formulário de contato no site da empresa',
    }
    return render(request, 'sobre.html', dados)

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')
