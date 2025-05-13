terrestres = []
with open('aula05/exercicios/animais.txt', encoding='utf8') as arq:
    for linha in arq:
        animal, habitat = linha.strip().split(',')
        if habitat == 'terrestre':
            terrestres.append(animal)

with open('aula05/exercicios/animais_terrestres.txt', 'w', encoding='utf8') as arq:
    for animal in terrestres:
        arq.write(f'{animal}\n')

# alternativa (com um único with)

with open('aula05/exercicios/animais.txt', encoding='utf8') as arq_animais,\
     open('aula05/exercicios/animais_terrestres.txt', 'w', encoding='utf8') as arq_terrestres:
    for linha in arq_animais:
        animal, habitat = linha.strip().split(',')
        if habitat == 'terrestre':
            arq_terrestres.write(f'{animal}\n')
