anos_bissextos = [2020,1988,2028,2040,1996]
ano = input("Digite um ano:")

if int(ano) in anos_bissextos:
    print('O ano é bissexto')

else:
    print('Não é bissexto')