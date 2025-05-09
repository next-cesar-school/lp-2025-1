numeros = [1, 2, 3, 4, 5, 6]

print(numeros)

numeros_pares = list(filter(lambda n: n % 2 == 0, numeros))

print(numeros_pares)

palavras = ["sol", "lua", "estrelas", "mar", "céu"]

palavras_filtradas = list(filter(lambda p: len(p) == 3, palavras))

print(palavras_filtradas)