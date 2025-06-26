# -*- coding: utf-8 -*-

# dicionário com o mapeamento completo da classificação
classificacao = {
    'vertebrado-ave-carnivoro': 'aguia',
    'vertebrado-ave-onivoro': 'pomba',
    'vertebrado-mamifero-onivoro': 'homem',
    'vertebrado-mamifero-herbivoro': 'vaca',
    'invertebrado-inseto-hematofago': 'pulga',
    'invertebrado-inseto-herbivoro': 'lagarta',
    'invertebrado-anelideo-hematofago': 'sanguessuga',
    'invertebrado-anelideo-onivoro': 'minhoca'
}

entrada = []
for _ in range(3):
    entrada.append(input())

# transforma a entrada em um único texto, separado por "-"
chave = '-'.join(entrada)

print(classificacao[chave])
