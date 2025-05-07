'''Crie uma lista chamada `quadrados` que contenha os quadrados dos números de 1 a 10
utilizando compreensão de listas.'''


numeros = list(range(1, 11))
quadrados = [n**2 for n in numeros]

print(quadrados)
