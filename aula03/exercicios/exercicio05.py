def print_inverso(lista):
    for valor in lista[::-1]:
      print(valor)

def get_valores():
    lista = []
    for idx in range(5):
        lista.append(int(input("Digite um valor: ")))
    return lista

lista = get_valores()
print_inverso(lista)
