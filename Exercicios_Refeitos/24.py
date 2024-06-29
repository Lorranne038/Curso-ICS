def troca_valores(a,b):
    temp = a
    a = b
    b = temp
    return a, b

valores = troca_valores(24, 15)

print(valores)