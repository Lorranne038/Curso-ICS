def calcula_par_impar(numero):
    lista_numeros_impar = '1, 3, 5, 7, 9' 
    ultimo_numero = numero[-1]

    if ultimo_numero in lista_numeros_impar:
        return 'impar'
    
    else:
        return 'par'
    
res = calcula_par_impar('13')
print(res)

while True:

    numero_digitado = input('Digite um numero para testar: ')
    res = calcula_par_impar(numero_digitado)
    print(res)