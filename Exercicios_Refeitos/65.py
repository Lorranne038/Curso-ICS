matriz_numeros = [1,2,3,4,5]

def sublista(lista):
    maior_numero = lista[-1]

    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero
        
res = sublista(matriz_numeros)
print(res)