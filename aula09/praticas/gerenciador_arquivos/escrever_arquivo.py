def escrever(caminho, conteudo):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
