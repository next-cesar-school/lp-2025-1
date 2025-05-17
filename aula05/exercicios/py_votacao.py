votos = []
# cria uma lista apenas com os candidados que receberam votos
with open('aula05/exercicios/dados_eleicao.csv') as dados:
    for linha in dados.readlines()[1:]:
        candidato = linha.split(',')[2].strip()
        #print(candidato)
        votos.append(candidato)

candidatos = set(votos) # cria um set, com o nome de cada candidato uma vez
cand_voto = dict()
# cria um dicionário com 'nome candidato' x 'quantidade votos'
for candidato in candidatos:
    cand_voto[candidato] = votos.count(candidato)

# organiza o dicionário usando uma função personalizada
cand_voto = sorted(cand_voto.items(), key=lambda x:x[1], reverse=True)

# cria o arquivo com os resultados
with open('aula05/exercicios/resultado.txt', 'w') as result:
    result.write('Resultados eleitorais\n')
    result.write('-' * 25 + '\n')
    result.write(f'Total de votos: {len(votos)}\n')
    result.write('-' * 25 + '\n')
    for cand in cand_voto:
        result.write(f'{cand[0]}: {(cand[1] * 100)/len(votos):.1f}% ({cand[1]})\n')
    result.write('-' * 25 + '\n')
    result.write(f'Vencedor: {cand_voto[0][0]}\n')
    result.write('-' * 25 + '\n')
