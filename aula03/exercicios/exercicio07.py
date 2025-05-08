def desenha_padrao(n):
    for i in range(1, n + 1):
        print(f'{i} ' * i)

numero = int(input('Informe um número: '))
desenha_padrao(numero)
