def elemento_inverso(lista):
    contador = len(lista) -1
    auxilio = []

    while contador >= 0:
        numero = lista[contador]
        auxilio.append(numero)
        contador = contador-1
    return auxilio

lista_invertida = elemento_inverso([1, 2, 3, 4, 5])
print(lista_invertida)
