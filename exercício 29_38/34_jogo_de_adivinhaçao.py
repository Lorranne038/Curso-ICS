numero_secreto = 5
numero_usuario = int(input('Advinhe o número: '))


if numero_secreto < numero_usuario:
     print('O numero secreto é menor') 

if numero_secreto > numero_usuario:
    print('O numero secreto é maior')

elif numero_secreto == numero_usuario:
    print('Parabéns vc acertou')
    
    
