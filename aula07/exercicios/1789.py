# -*- coding: utf-8 -*-

while True:
  try:
    _ = input()
    velocidades = map(int, input().split())

    maior_velo = max(velocidades)

    if maior_velo < 10:
      print(1)
    elif maior_velo < 20:
      print(2)
    else:
      print(3)
  
  except EOFError:
    break
