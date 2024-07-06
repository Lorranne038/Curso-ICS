temperaturas = [23,20,19,22,30,25]

maior = temperaturas[0]
menor = temperaturas[0]
contador = 0

while contador < len(temperaturas):
    temperatura = temperaturas[contador]
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura

    contador += 1

    print('A maior temperatura é ' + str(maior))        
    print('A menor temperatura é ' + str(menor))