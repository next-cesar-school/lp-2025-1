def maior_menor(numeros):
    
    def maior_numero(valores):
        return max(valores)
    
    def menor_numero(valores):
        return min(valores)
    
    if len(numeros) < 10:
        print('A lista é muito pequena')
        return None
    
    return maior_numero(numeros), menor_numero(numeros)

l = [1, 2, 3, 4, 5]
print(maior_menor(l))
