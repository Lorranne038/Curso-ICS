numero = 6
adivinhe = int(input("Adivinhe o número secreto: "))

if numero < adivinhe:
    print("O número é menor")
elif numero == adivinhe:
    print('Você acertou')    
elif numero > adivinhe:
    print("O número é maior")   