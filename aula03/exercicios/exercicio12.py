import random


def embaralha(texto):
    embaralha = random.sample(texto, len(texto))
    novo_texto = ''.join(embaralha)
    return novo_texto

texto = input("Digite um texto: ")
print(embaralha(texto))
