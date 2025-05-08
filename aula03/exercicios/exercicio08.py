def desenha_padrao(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end = " ")
        print()


numero = int(input('Informe um número: '))
desenha_padrao(numero)
