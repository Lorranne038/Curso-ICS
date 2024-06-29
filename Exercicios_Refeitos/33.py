nota1 = input("Digite a primeira nota:")
nota2 = input("Digite a segunda nota:")
nota3 = input("Digite a terceira nota:")
nota4 = input("Digite a quarta nota:")
nota5 = input("Digite a quinta nota:")


res = int(nota1 + nota2 + nota3 + nota4 + nota5) /4

if res >= 7:
    print('Acima da media')

elif 4<= res <7:
    print('Na media') 

else:       
     print('Reprovado') 