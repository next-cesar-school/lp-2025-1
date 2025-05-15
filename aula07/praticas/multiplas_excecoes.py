def receber_numero():
    n_tentativas = 3
    while n_tentativas > 0:
        try:
            print(f'{n_tentativas=}')
            numero = int(input('Insira o número: '))
            print(10/numero)
        except ValueError:
            print('🚨 Não foi possível converter o valor em número inteiro.')
        except ZeroDivisionError:
            print('🚨 Não é possível dividir por zero.')
        else:
            print('Deu tudo certo, familia ✌️')
            return numero
        finally:
            n_tentativas -= 1

print(f'Valor retornado: {receber_numero()}')
print('Programa encerrado.')

'''flag = False
i = 0
while i < 3:
    print(f'{i}')
    i += 1
    if i == 2:
        flag = True
        break
else:
    print('Acabou o programa')

if flag:
    print('O While foi interrompido de forma igonrante com um break')
'''