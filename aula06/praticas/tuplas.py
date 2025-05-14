lista_dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
tupla_dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')

print(type(lista_dias))
print(type(tupla_dias))

# tuple -> Tópicos a explorar:
# - Criação de uma Tupla
valores = [11101010, 33455654]
coordenadas = tuple(valores)

print(coordenadas, type(coordenadas))

# - Acesso aos elementos de uma Tupla
print(coordenadas[0])
print(tupla_dias[:3])
print(tupla_dias[::2])

# - len()
print(len(tupla_dias))
print(len(coordenadas))

# - tupla.index(item)
print(tupla_dias.index('sábado'))

# - tupla.count(item)
print(tupla_dias.count('domingo'))

# - Imutabilidade
#tupla_dias[5] = 'sábado'
#tupla_dias.add('domingo-feira')
print(tupla_dias)

#nova_lista = list(tupla_dias)
