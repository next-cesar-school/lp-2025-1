# -*- coding: utf-8 -*-


n1 = int(input())
n2 = int(input())

lista = []

if n2 < n1:
    n1, n2 = n2, n1

lista = [n for n in range(n1+1, n2) if n % 2 != 0]

print(sum(lista))
