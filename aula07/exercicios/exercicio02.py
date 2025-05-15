def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print('== Conteúdo do arquivo: ==')
            print(conteudo)
    except FileNotFoundError:
        print(f'Erro: O arquivo "{nome_arquivo}" não foi encontrado.')
    finally:
        print('Tentativa de leitura concluída.')

# Teste da função
nome_arquivo = input('Insira o nome do arquivo com a extensão: ')
ler_arquivo(nome_arquivo)
