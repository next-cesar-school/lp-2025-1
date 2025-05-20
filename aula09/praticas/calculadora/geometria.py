from math import pi


def area_circulo(raio):
    return pi * raio ** 2

def area_retangulo(base, altura):
    return base * altura

def area_quadrado(lado):
    return area_retangulo(lado, lado)
