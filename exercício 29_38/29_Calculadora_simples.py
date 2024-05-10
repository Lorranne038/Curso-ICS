
num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundo numero: ')

operaçao = input('Digite qual operação vc deseja: + - * /')
print(num1, num2, operaçao)

if operaçao =="+":
    soma = int (num1)+int(num2)
    print(soma)

elif operaçao =='-':
    subtraçao = int(num1) - int(num2)
    print(subtraçao)

elif operaçao =='*':
    multiplicaçao = int(num1) * int(num2)
    print(multiplicaçao)

elif operaçao == "/":   
    divisao = int(num1) / int(num2)
    print(divisao)