# -*- coding: utf-8 -*-

while True:
    try:
        expressao = input()
        cont = 0
        for l in expressao:
            if l == '(':
                cont += 1
            elif l == ')':
                cont -= 1
            
            if cont < 0:
                break
        
        if cont != 0:
            print('incorrect')
        else:
            print('correct')
    except EOFError:
        break
