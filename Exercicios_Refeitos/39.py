lista = "1,3,5,7,9"
def par_impar(valor):
    ajuda = []
    ultimo_digito = valor[-1]

    for ultimo_digito in lista:
        digite = input('Digite um número: ')
    ajuda.append(int(digite))
    if ultimo_digito in  lista:
     print("impar")
    else:
        print("par")
par_impar(lista)        