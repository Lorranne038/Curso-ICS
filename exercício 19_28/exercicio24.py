def troca_valores(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b
troca = troca_valores(14, 12)
print(troca)