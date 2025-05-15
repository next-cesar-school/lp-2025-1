def buscar_chave(dicionario, chave):
    try:
        valor = dicionario[chave]
    except KeyError:
        print(f'Erro: A chave "{chave}" não foi encontrada no dicionário.')
    else:
        print(f'Valor encontrado: {valor}')
    finally:
        print('Operação de busca concluída.')

# Teste da função
meu_dicionario = {'nome': 'João', 'idade': 31, 'cidade': 'Recife'}

buscar_chave(meu_dicionario, 'idade')  # Deve encontrar
buscar_chave(meu_dicionario, 'profissao')  # Deve gerar erro
