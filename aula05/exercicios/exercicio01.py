with open('aula05/exercicios/animais.txt', encoding='utf8') as arq:
    for linha in arq:
        animal, habitat = linha.strip().split(',')
        if habitat == 'terrestre':
            print(animal)

# Bônus
habitat_alvo = input('Informe o habitat: ').lower()

with open('aula05/exercicios/animais.txt', encoding='utf8') as arq:
    for linha in arq:
        animal, habitat = linha.strip().split(',')
        if habitat == habitat_alvo:
            print(animal)
