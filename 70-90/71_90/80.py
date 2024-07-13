'''
*Combinação de Dicionários*
- Crie dois dicionários e combine-os em um único dicionário. Exiba o dicionário resultante.
'''
dados = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasília',
    'Haiti': 'Porto príncipe',
    'Estados Unidos': 'Washington',
    'Peru': 'Lima',
    'França' : 'Paris',
    'Portugal': 'Lisboa',
    'Itália': 'Roma',
}
print(dados)

dicionario = {
    'sarah': {
        'idade' :[14],
        'cidade':['Buritizeiro'],
        'religiao':['Catolica']
    },
    'enzo': {
        'idade' :[12],
        'cidade':['Buritizeiro'],
        'religiao':['Catolica']
    },
    'dulce': {
        'idade' :[34],
        'cidade':['Buritizeiro'],
        'religiao':['Catolica']
    }    
}
print(dicionario)

print(dados, dicionario)