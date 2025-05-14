palavras = {'dog': 'cão',
            'bird': 'pássaro',
            'lion':'leão'}

#print(palavras)

# Tópicos a explorar
# - Criando um dicionário
#palavras = dict()

palavras['bear'] = 'urso'
palavras['elephant'] = 'elefante'

print(palavras)

# - Acessando elementos de um dicionário

print(palavras['bird'])
print(palavras['bear'])

# - Adição de itens por atribuição
palavras['dog'] = 'cachorro'

#print(palavras[2])

# - Adição de itens por update

dados = [('crocodille', 'crocodilo'), ('monkey', 'macaco')]
palavras.update(dados)

# - Removendo itens

palavras.pop('bird')
palavras.popitem()

# - esvaziando um dicionário
#palavras.clear()

print(palavras)

# Tópicos a explorar
# - get()
print(palavras.get('efalante', 'Elemento não encontrado'))

# - keys()
print(palavras.keys())

# - values()
print(palavras.values())

# - items()
print(palavras.items())

# - for
for chave, valor in palavras.items():
    print(f'A chave é {chave} que tem o valor {valor}')

notas = dict()
for _ in range(3):
    nome, nota = input('Insira o nome e a nota da pessoa: ').split()
    notas[nome] = float(nota)

print(notas)
