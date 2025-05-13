data = []
lp = []
# armazena a data em um vetor e o lucro/prejuízo em outro
with open('aula05/exercicios/dados_financeiros.csv') as dados:
    for line in dados.readlines()[1:]:
        d, r = line.split(',')
        data.append(d)
        lp.append(int(r))

variacao = []
i = 0
# calcula as variações entre os meses
while i < len(lp) - 1:
    variacao.append(lp[i+1] - lp[i])
    i += 1

total_meses = len(data)
total = sum(lp)

# arquivo de saída
with open('aula05/exercicios/relatorio.txt', 'w', encoding='utf8') as result:
    result.write('Analise financeira\n')
    result.write('-' * 28 + '\n')
    result.write(f'Total de meses: {total_meses}\n')
    result.write(f'Total: $ {total}\n')
    result.write(f'Média: $ {total/total_meses:.2f}\n')
    result.write(f'Variação da média: $ {sum(variacao)/len(variacao):.2f}\n')
    result.write(f'Maior aumento nos lucros: {data[variacao.index(max(variacao)) + 1]} ($ {max(variacao)})\n')
    result.write(f'Maior redução nos lucros: {data[variacao.index(min(variacao)) + 1]} ($ {min(variacao)})\n')
