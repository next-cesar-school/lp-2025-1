# -*- coding: utf-8 -*-

cifra = {'@': 'a',
         '&': 'e',
         '!': 'i',
         '*': 'o',
         '#': 'u'}

while True:
    try:
        texto = input()
        novo_texto = ''
        for letra in texto:
            if letra in cifra.keys():
                novo_texto += cifra[letra]
            else:
                novo_texto += letra

        print(novo_texto)
    except EOFError:
        break
