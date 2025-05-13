with open('aula05/praticas/dados.txt', 'w', encoding='utf-8') as dados:
    while True:
        entrada = input('Insira um nome: ')
        
        if entrada.lower() == 'sair':
            break
        
        dados.write(f'{entrada}\n')

print(':: PROGRAMA ENCERRADO ::')

with open('a.txt', 'w') as a, open('b.txt', 'w') as b:
    a.write('AAAAAAAAA')
    b.write('BBBBBBBBBB')
