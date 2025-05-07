numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_multiplicados = []

for n in numeros:
    if n % 2 == 0:
        numeros_multiplicados.append(n * 2)
    else:
        numeros_multiplicados.append(n)

print(numeros_multiplicados)

#numeros_mult = [n * 2 for n in numeros if n % 2 == 0]
numeros_mult = [n * 2 if n % 2 == 0 else n for n in numeros]

print(numeros_mult)