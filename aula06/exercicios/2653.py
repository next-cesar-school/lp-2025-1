# -*- coding: utf-8 -*-


joias = set()

while True:
  try:
    joias.add(input())
  except EOFError:
    break

print(len(joias))
