def e_palindro(palavra):
    return palavra == palavra[::-1]

palavra = input('Informe uma palavra: ')
resultado = "é palindro" if e_palindro(palavra) else "não é palindro"
print(resultado)
