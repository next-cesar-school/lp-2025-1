nomes = ['Jorge', 'Erick', 'Zna', 'Amariana']

'''def avalia_tamanho(valor):
    return len(valor)

nomes.sort(key=avalia_tamanho)'''
nomes.sort(key=lambda valor: len(valor))

print(nomes)
