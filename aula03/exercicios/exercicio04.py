def fahrenheit_celsius(f):
    return (f - 32) / 1.8

def celsius_fahrenheit(c):
    return c * 1.8 + 32

temp = float(input("Digite uma temperatura: "))
tipo = input("Qual a temperatura (celsius/fahrenheit): ")

if tipo == 'celsius':
    print(celsius_fahrenheit(temp))
elif tipo == 'fahrenheit':
    print(fahrenheit_celsius(temp))
