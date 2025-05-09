valores = input('Insira as notas: ').split()

print(valores)

novos_valores = list(map(float, valores))

print(novos_valores)


valores = list(map(float, input().split()))
