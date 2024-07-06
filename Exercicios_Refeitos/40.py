lista = [
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7),
    (8),
    (9),
    (10)
]

for par in range(0, len(lista)):
    numero = lista[par]
    if numero %2 == 0:
        print(str(numero))