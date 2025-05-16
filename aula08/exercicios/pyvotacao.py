import csv
from collections import Counter          # só para contar de forma eficiente

# Leitura e contagem dos votos
with open('aula08/exercicios/dados_eleicao.csv', encoding='utf-8') as dados:
    leitor = csv.DictReader(dados)

    # a chave de interesse é 'Candidato'
    contador = Counter(linha['Candidato'] for linha in leitor)

total_votos = sum(contador.values())      # total de votos apurados

# Construção dos registros para gravar
# dict-comprehension que devolve: {candidato, percentual, quantidade de votos}
registros = {
    cand: {
        'candidato': cand,
        'percentual': f'{(qtde / total_votos) * 100:.1f}%',
        'quantidade de votos': qtde
    }
    for cand, qtde in contador.items()
}

# Coloca os dados em ordem decrescente de votos:
registros_ordenados = sorted(registros.values(), key=lambda r: r['quantidade de votos'], reverse=True)

# Escrita do CSV de saída
with open('aula08/exercicios/resultado.csv', 'w', newline='', encoding='utf-8') as arq_saida:
    campos = ['candidato', 'percentual', 'quantidade de votos']
    escritor = csv.DictWriter(arq_saida, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(registros_ordenados)
