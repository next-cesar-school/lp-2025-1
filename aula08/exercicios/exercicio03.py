from random import randint


def rolar_dado():
    valor = randint(1, 6)
    print(f"Resultado do dado: {valor}")

    if valor == 6:
        print('Dano Crítico!')

rolar_dado()
