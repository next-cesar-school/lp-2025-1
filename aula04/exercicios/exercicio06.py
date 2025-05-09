from functools import reduce


numeros = [1, 2, 3, 4]

quadrados = map(lambda x: x**2, numeros)
somas = reduce(lambda x, y: x + y, quadrados)

print(somas)
