
from math import isqrt


def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = isqrt(n)
    for valor in range(3, limite + 1, 2):  # percorre apenas ímpares
        if n % valor == 0:
            return False
    return True

def fatorial(n):
    if n < 0:
        return None # o número não pode ser menor que zero (o correto seria dar erro)
    if n in (0, 1):
        return 1

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
