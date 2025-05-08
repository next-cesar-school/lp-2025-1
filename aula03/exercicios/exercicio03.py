def procura(lista, nome):
    for texto in lista:
        if texto == nome:
            return True
    return False

lista = ["fabricio", "carlos", "ana", "maria"]

nome = input("Digite um nome a ser buscado: ")

print(procura(lista, nome))
