def acha_maior_lista(lista):
    maior_numero = lista[0]

    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero

def coleta_notas_alunos():
    notas = []
    for nota_digitada in range(0, 9):
        nota_digitada = input('Digite a nota: ')
        notas.append(int(nota_digitada))

    return notas

notas = coleta_notas_alunos()       
maior = acha_maior_lista(notas)
print(maior)

