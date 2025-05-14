numeros = set()

numeros.add(1)
numeros.add(2)
numeros.add(3)
numeros.add(1)
numeros.add(3)
numeros.add(4)
numeros.add(3)
numeros.add(2)
numeros.add(1)
numeros.add(3)

print(numeros)

ingredientes = {'bacon', 'banana', 'spam', 'ovos', 'spam', 'salsicha', 'spam'}

print(ingredientes)

# Tópicos a explorar:
# - criar um set
# - print(ingredientes[0]) # erro!

#print(ingredientes[0])

# - adicionar elementos
ingredientes.add('tomate')

# - remover elementos
ingredientes.remove('spam')

print(ingredientes)
