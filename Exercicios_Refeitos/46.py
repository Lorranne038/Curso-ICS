lista = [5,3,9,1,10]

def acha_maior(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior
        
res = acha_maior(lista)
print(res)