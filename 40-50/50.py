
def reverte_lista(lista):
    contador = len(lista) -1
    lista_auxiliar = []

    while contador >= 0:
        numero = lista[contador]
        lista_auxiliar.append(numero)
        contador = contador-1
    return lista_auxiliar

lista_invertida = reverte_lista([1, 2, 3, 4, 5])
print(lista_invertida)










