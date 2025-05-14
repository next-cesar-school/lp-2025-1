ceps = {}
def inclui_endereco():
    cep = input('Insira um CEP: ')
    endereco = input(f'Insira um endereço do CEP {cep}: ')

    ceps.update({cep:endereco})


def busca_endereco():
    cep = input('Insira um CEP que você deseja buscar: ')

    print(ceps.get(cep, 'CEP não encontrado'))

while True:
    entrada = input('O que você deseja fazer:\n\t1 - Inserir um CEP\n\t2 - Buscar um CEP\n\t3 - Sair\n')

    if entrada == '1':
        inclui_endereco()
    elif entrada == '2':
        busca_endereco()
    elif entrada == '3':
        print('Volte sempre!')
        break
    else:
        print('Comando inválido, tente novamente...')

    print(ceps)
