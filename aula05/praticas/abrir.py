arquivo = open('aula05/praticas/exemplo.txt', 'r', encoding='utf-8')

#print(arquivo.read()) # lê o arquivo todo

#print(arquivo.readline()) # lê uma linha do arquivo

#arquivo.seek(1) # move o cursor para uma posição em bytes

#linhas = arquivo.readlines() # retorna todo o arquivo como uma lista de strings
#print(linhas)

for linha in arquivo:
    print(linha)
    if 'pamonha' in linha:
        print('Achei a pamonha!')
        break
