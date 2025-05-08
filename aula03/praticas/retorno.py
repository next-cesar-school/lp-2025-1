def soma(a, b):
    return a + b

resultado = soma(10, 5)

print(f'Valor do resultado: {resultado}')

if resultado > 10:
    print('Resultado maior que 10')
else:
    print('Resultado menor que 10')







lista = [1, 2, 3, 4, 5]
tamanho = len(lista)

print(f'O tamanho da lista é de {tamanho} elementos')

if tamanho >= 3:
    print('A lista tem 3 ou mais elementos')
else:
    print('A lista tem menos de 3 elementos')



input('Digite o seu nome: ')

def procura_negativo(numeros):
    for numero in numeros:
        if numero < 0:
            print(f'Núemro negativo {numero} foi encontrado')
            return True
    
    return False

valores = [1, 2, 3, 4, 5]

resultado = procura_negativo(valores)


