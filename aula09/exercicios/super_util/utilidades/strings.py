def contar_vogais(texto):
    # contar o número de vogais em uma string
    vogais = set('aeiou')
    
    return sum(1 for c in texto.lower() if c in vogais)

def inverter(texto):
    # inverter uma string
    return texto[::-1]
