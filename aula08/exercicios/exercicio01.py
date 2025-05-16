from math import pi, pow


def calcular_area_circunferencia(r):
    area = pi * (pow(r, 2))
    print(f"A área da circunferência com raio {r:.3f} é: {area:.3f}")

raio = float(input("Informe o valor do raio: "))
calcular_area_circunferencia(raio)
