'''with open('notas.txt', 'w') as notas:
    for _ in range(4):
        notas.write(f'{input("Insira a nota: ")}\n')

with open('notas.txt') as notas:
    result = []
    for linha in notas:
        result.append(int(linha))
    
    print(f'A maior nota é {max(result)}')
    print(f'A menor nota é {min(result)}')
    print(f'A média nota é {sum(result)/len(result)}')'''

# melhores práticas

notas = []
for _ in range(4):
    notas.append(f'{input("Insira a nota: ")}')

with open('aula05/exercicios/notas.txt', 'w') as arq_notas:
    arq_notas.writelines('\n'.join(notas))
    arq_notas.write('\n')

notas_lidas = []
with open('aula05/exercicios/notas.txt') as arq_notas:
    for nota in arq_notas:
        notas_lidas.append(float(nota))

print(f'Maior nota: {max(notas_lidas)}')
print(f'Menor nota: {min(notas_lidas)}')
print(f'Média: {sum(notas_lidas)/len(notas_lidas)}')
