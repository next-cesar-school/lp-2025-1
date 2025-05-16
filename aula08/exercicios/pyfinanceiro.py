import csv


# Listas para armazenar os dados
data = []
lp = []

# Lê os dados do arquivo CSV
with open('aula08/exercicios/dados_financeiros.csv', 'r') as dados:
    leitor = csv.reader(dados)
    next(leitor)  # Pula o cabeçalho
    for linha in leitor:
        data.append(linha[0])  # Data
        lp.append(int(linha[1]))  # Lucro/Prejuízo

# Calcula as variações entre os meses
variacao = [lp[i+1] - lp[i] for i in range(len(lp) - 1)]

# Calcula os totais e médias
total_meses = len(data)
total = sum(lp)
media = total / total_meses
media_variacao = sum(variacao) / len(variacao)
maior_aumento = max(variacao)
maior_reducao = min(variacao)

# Identifica os meses do maior aumento e maior redução
mes_maior_aumento = data[variacao.index(maior_aumento) + 1]
mes_maior_reducao = data[variacao.index(maior_reducao) + 1]

# Escreve o relatório em um arquivo CSV
with open('aula08/exercicios/relatorio.csv', 'w', newline='', encoding='utf8') as result:
    escritor = csv.writer(result)
    escritor.writerow(['Análise Financeira'])
    escritor.writerow(['-' * 28])
    escritor.writerow([f'Total de meses: {total_meses}'])
    escritor.writerow([f'Total: $ {total}'])
    escritor.writerow([f'Média: $ {media:.2f}'])
    escritor.writerow([f'Variação da média: $ {media_variacao:.2f}'])
    escritor.writerow([f'Maior aumento nos lucros: {mes_maior_aumento} ($ {maior_aumento})'])
    escritor.writerow([f'Maior redução nos lucros: {mes_maior_reducao} ($ {maior_reducao})'])
