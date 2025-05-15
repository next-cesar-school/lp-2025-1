import csv


with open("aula08/praticas/dados_financeiros.csv", "r") as arquivo:
    #leitor = csv.reader(arquivo)
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['Data'], linha['Lucros/Perdas'])


dados = [
    ["Nome", "Idade", "Cidade"],
    ["Frederico", 30, "Recife"],
    ["Ana", 25, "São Paulo"],
    ["Beto", 35, "Olinda"]
]

with open("saida.csv", "w", newline="", encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)