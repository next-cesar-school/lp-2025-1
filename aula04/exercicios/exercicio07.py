from functools import reduce


palavras = ["sol", "montanha", "mar", "universo"]

mais_longa = reduce(lambda x, y: x if len(x) > len(y) else y, palavras)
print(mais_longa)
