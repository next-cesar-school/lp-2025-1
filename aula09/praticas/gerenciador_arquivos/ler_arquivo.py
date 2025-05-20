def ler(caminho):
    with open(caminho, encoding='utf-8') as arquivo:
        return arquivo.read()
