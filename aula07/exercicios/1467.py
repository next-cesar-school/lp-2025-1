# -*- coding: utf-8 -*-

while True:
    try:
        entrada = input().split()
        
        pos = -1
        if entrada.count('1') == 1:
            pos = entrada.index('1')
        elif entrada.count('0') == 1:
            pos = entrada.index('0')
        
        if pos == -1:
            print('*')
        else:
            print('ABC'[pos])
        
    except EOFError:
        break
