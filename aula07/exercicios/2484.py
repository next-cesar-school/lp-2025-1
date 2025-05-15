# -*- coding: utf-8 -*-

while True:
    try:
        p = list(input())
        esp = 0
        for _ in range(len(p)):
            print(' ' * esp, end='')
            print(*p, sep=' ')

            esp += 1
            p.pop()

        print()

    except EOFError:
        break
