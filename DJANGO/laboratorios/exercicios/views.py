from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ex1(request):
    frase = 'Olá, Mundo!'
    data = {
        'titulo': 'Exercicio 1. Olá Mundo.',
        'descricao_exercicio' : 'Faça um programa que mostre a frase Ola Mundo',
        'frase' : frase
    }
    return render (request, 'ex1.html', data)

def ex2(request):
    data = {
        'titulo': 'Exercicio 2. Calculo de total.',
        'descricao_exercicio' : 'Faça um programa que receba 2 numeros do usuario e calcule o total.',
    }

    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total = int(num1) + int (num2)

        data['total'] = total
    return render (request, 'ex2.html', data)


def ex3(request):
    data = {
        'titulo': 'Exercicio 3. Nome e Idade.',
        'descricao_exercicio' : 'Faça um programa que imprima o nome e idade.',
    }

    if request.method =='POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        frase = f'Seu nome é {nome} e sua idade é {idade}'

        data['frase'] = frase
    return render (request, 'ex3.html', data)

def ex4(request):
    data = {
        'titulo': 'Exercicio 4. Soma de dois Números.',
        'descricao_exercicio' : 'Faça um programa que faça a soma de dois números.',

    }
    if request.method =='POST':
        valor1 = request.POST.get('valor1')
        valor2 = request.POST.get('valor2')
        total = int(valor1) + int(valor2)
        
        data['total'] = total
    return render (request, 'ex4.html', data)

def ex5(request):
    data = {
        'titulo': 'Exercicio 5. Caracteres de uma Palavara.',
        'descricao_exercicio' : 'Faça um programa que imprima a quantidade de caracteres de uma palavra.',
    }

    if request.method =='POST':
        palavra = request.POST.get('palavra')
        caracteres = f'{len(palavra)}'

        data['caracteres'] = caracteres
    return render (request, 'ex5.html', data)

def ex6(request):
    data = {
        'titulo': 'Exercicio 6. Formar frases com 5 palavras .',
        'descricao_exercicio' : 'Faça um programa que imprima palavras como se fossem frases.',
    }
    if request.method =='POST':
        palavra1 = request.POST.get('palavra1')
        palavra2 = request.POST.get('palavra2')
        palavra3 = request.POST.get('palavra3')
        palavra4 = request.POST.get('palavra4')
        palavra5 = request.POST.get('palavra5')
        total = (palavra1) + (palavra2) + (palavra3) + (palavra4) + (palavra5)

        data['total'] = total

    return render (request, 'ex6.html', data)

def ex7(request):
    data = {
        'titulo': 'Exercicio 7. Número Somado dele mesmo.',
        'descricao_exercicio' : 'Faça um programa que imprima um numero somado dele mesmo.',

    }
    if request.method =='POST':
        numero = request.POST.get('numero')
        total = (numero) + (numero)
        
        data['total'] = total
    return render (request, 'ex7.html', data)

def ex8(request):
    data = {
        'titulo': 'Exercicio 8. Número somado mais 1.',
        'descricao_exercicio' : 'Faça um programa que faça a soma de um numero mais o numero 1.',

    }

    if request.method == 'POST':
        numero = request.POST.get('numero')
        total = int(numero) + 1
        data['total'] = total
    return render(request, 'ex8.html', data)

def ex9(request):
    data = {
        'titulo': 'Exercicio 9. Olá (nome).',
        'descricao_exercicio' : 'Crie um programa que declare uma variável nome com o seu nome e, exiba a mensagem "Olá, [nome]!".',
    }

    if request.method =='POST':
        nome = request.POST.get('nome')
        frase = f'Olá, {nome}!'

        data['frase'] = frase
    return render (request, 'ex9.html', data)

def ex10(request):
    data = {
        'titulo': 'Exercicio 10. Duas Variáveis Inteiras e Somar esses Valores.',
        'descricao_exercicio' : 'Crie um programa que tenha duas variáveis inteiras, some esses valores e imprima o resultado da soma.'

    }

    if request.method =='POST':
        valor1 = request.POST.get('valor1')
        valor2 = request.POST.get('valor2')
        total = int(valor1) + int(valor2)
        
        data['total'] = total
    return render (request, 'ex10.html', data)

def ex11(request):
    data = {
         
         'titulo':'Exercício 11',
         'descricao_exercicio':' Desenvolva um programa que tenha uma variável do tipo string com uma frase qualquer e, com print, mostre a quantidade de caracteres dessa frase'
     }

    if request.method == 'POST':
        palavra = request.POST.get("palavra") 
        caracteres = len(palavra)
        data['caracteres'] = caracteres
         
    return render(request, 'ex11.html', data)

def ex12(request):
    data = {
         'titulo':'Exercício 12',
         'descricao_exercicio':' Faça um programa que contenha duas variáveis string, parte1 e parte2, atribua valores a elas, una as duas em uma terceira variável e imprima o resultado'
    }
    if request.method == 'POST':
        parte1 = request.POST.get("parte1") 
        parte2 = request.POST.get("parte2")
        parte3 = str(parte1) + " " + str(parte2)
        data['parte3'] = parte3
    return render (request, 'ex12.html', data)

def ex13(request):
    data = {
         'titulo':'Exercício 13',
         'descricao_exercicio':'Crie um programa que tenha uma variável com o ano atual e outra com o ano de nascimento de uma pessoa (use valores fictícios) e imprima a idade dessa pessoa'
    }
    if request.method == 'POST':
        Ano_de_nascimento = request.POST.get("ano_de_nascimento") 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(Ano_de_nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex13.html', data)


def ex14(request):
    data = {
         'titulo':'Exercício 14',
         'descricao_exercicio':'Escreva um programa que tenha duas variáveis a e b com valores numéricos, troque os valores entre elas e, em seguida, imprima os novos valores de a e b'
    }
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex14.html', data)

def ex15(request):
    data = {
         'titulo':'Exercício 15',
         'descricao_exercicio':' Desenvolva um programa que crie uma variável frase e atribua a ela uma string qualquer. Imprima essa string três vezes seguidas'
    }
    if request.method == 'POST':
        frase = request.POST.get("frase") 
        frase1 = str(frase) + ' ' + str(frase) + ' ' + str(frase)
        data['frase1'] = frase1
    return render(request, 'ex15.html', data)

def ex16(request):
    data = {
         'titulo':'Exercício 16',
         'descricao_exercicio':'Faça um programa que declare quatro variáveis inteiras, realize a média desses valores e imprima o resultado'
    }
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        valor3 = request.POST.get("valor3") 
        valor4 = request.POST.get("valor4")
        media = (int(valor1) + int(valor2) + int(valor3) + int(valor4))/4
        data['media'] = media
    return render (request, 'ex16.html', data)

def ex17(request):
    data = {
         'titulo':'Exercício 17',
         'descricao_exercicio':'Crie um programa que tenha uma variável com uma string representando o nome de uma cor e outra variável com um objeto (por exemplo, "carro"). Imprima uma frase que combine essas informações, como "carro azul"'
    }
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " " + str(palavra1) + " " 
        data['frase'] = frase
    return render (request, 'ex17.html', data)

def ex18(request):
    data = {
        'titulo':'Exercício 18',
         'descricao_exercicio':'Escreva um programa que declare duas variáveis com nomes de cidades e use print para exibir uma frase que diga que uma está a leste da outra, por exemplo, "Paris está a leste de Londres'
    }
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " está a leste de " + str(palavra1)
        data['frase'] = frase
    return render(request, 'ex18.html', data)

def ex19(request):
    data = {
        'titulo':'Exercício 19',
         'descricao':'Escreva uma função chamada saudacao que aceite um nome como argumento e imprima "Olá, [nome]!"'
    }
    
    if request.method =='POST':
        nome = request.POST.get('nome')
        saudacao = f'Olá, {nome}!'

        data['saudacao'] = saudacao
    return render (request, 'ex19.html', data)

def ex20(request):
    data = {
        'titulo':'Exercício 20',
         'descricao_exercicio':'Crie uma função chamada soma que receba dois números como parâmetros e retorne a soma desses dois números'
    }
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        total = int(valor1) + int(valor2)
        data['total'] = total
    return render(request, 'ex20.html', data)

def ex21(request):
    data = {
        'titulo':'Exercício 21',
         'descricao_exercicio':'Desenvolva uma função conta_caracteres que receba uma string como argumento e retorne o número de caracteres na string.'
    }
    if request.method == 'POST':
        palavra = request.POST.get('palavra') 
        caracteres = len(palavra)
        data['caracteres'] = caracteres
         
    return render(request, 'ex21.html', data)

def ex22(request):
    data = {
        'titulo':'Exercicios 22',
        'descricao_exercicio':' Faça uma função chamada concatena que receba duas strings, parte1 e parte2, como parâmetros, una-as em uma nova string e retorne essa nova string.'
    }
    if request.method == 'POST':
        parte1 = request.POST.get('parte1') 
        parte2 = request.POST.get('parte2')
        total = int(parte1) + int(parte2)
        data['total'] = total
         
    return render(request, 'ex22.html', data)

def ex23(request):
    data = {
         'titulo':'Exercício 23',
         'descricao_exercicio':'Escreva uma função chamada calcula_idade que receba o ano atual e o ano de nascimento, e retorne a idade da pessoa.'
    }
    if request.method == 'POST':
        nascimento = request.POST.get('nascimento') 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex23.html', data)

def ex24(request):
    data = {
        'titulo':'Exercício 24',
        'descricao_exercicio':'Crie uma função chamada troca_valores que receba dois valores a e b como parâmetros, troque os valores entre eles e retorne ambos.'
    }
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex24.html', data)

def ex25(request):
    data = {
        'titulo':'Exercício 25',
        'descricao_exercicio':'Desenvolva uma função chamada repete_string que receba uma string frase e um número inteiro n, e retorne a string repetida n vezes.'
    }
    if request.method == 'POST':
        frase = request.POST.get('frase')
        string = str(frase) *3
        data['total'] = string
    return render(request, 'ex25.html', data)    


        
        
    

