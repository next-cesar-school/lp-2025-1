# -*- coding: utf-8 -*-


c = int(input())

def printImpares(n, m):
    total = 0
    for i in range(n+1, m):
        if i % 2 != 0:
            total += i
    print(total)

for _ in range(c):
    n, m = [int(v) for v in input().split()]

    if n > m:
        n, m = m, n

    printImpares(n, m)
