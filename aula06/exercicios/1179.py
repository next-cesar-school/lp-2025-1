# -*- coding: utf-8 -*-

def esvaziar(lista, texto):
    """Esvazia toda a lista, exibindo os valores que tinham nele"""

    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        print(f'{texto}[{i}] = {lista.pop(0)}')

impar, par = [], []

for _ in range(15):
    numero = int(input())

    par.append(numero) if numero % 2 == 0 else impar.append(numero)

    if len(par) == 5:
        esvaziar(par, 'par')

    if len(impar) == 5:
        esvaziar(impar, 'impar')

esvaziar(impar, 'impar')
esvaziar(par, 'par')
