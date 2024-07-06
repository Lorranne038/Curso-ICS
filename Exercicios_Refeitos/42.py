cor = ['Amarelo', 'Azul','Vermelho','Verde','Preto','Branco']

def caracteres(palavra):
    
    for valor in palavra:
        if len(valor)> 4:
            print(valor)
caracteres(cor) 
