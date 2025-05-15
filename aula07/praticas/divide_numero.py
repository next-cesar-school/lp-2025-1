def dividir(num1, num2):
    try:
        retorno = num1 / num2
        return retorno
    except ZeroDivisionError:
        print('Não é possível dividir por zero!')

try:
    a = int(input('Insira o 1º número: '))
    b = int(input('Insira o 2º número: '))
    
    resultado = dividir(a, b)
    print(resultado)
except ValueError:
    print('Ocorreu um erro ao converter o número para inteiro')
