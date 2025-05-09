from functools import reduce

numeros = [1, 2, 3, 4, 5]

soma = reduce(lambda a, b: a * b, numeros)

print(soma)
