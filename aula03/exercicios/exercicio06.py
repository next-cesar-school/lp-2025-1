def invertedor(lista):
    lista_invertida = []
    for x in range(1,len(lista)+1):
        lista_invertida.append(lista[-x])
    return lista_invertida

lista = [1,2,3,4,5]
invertedor(lista)
