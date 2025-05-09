numeros = list(range(2, 20))

primos = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numeros))

print(primos)
