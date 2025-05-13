arquivo = open('aula05/praticas/teste.txt', 'a')

'''arquivo.write('Primeira linha do arquivo...\n')
arquivo.write('Segunda linha do arquivo\n')
arquivo.write('Terceira linha do arquivo!\n')'''

arquivo.write('Essa vai ser massa...!\n')

informacoes = ['aaaaaaa', 'bbbbbbb', 'cccccc', 'dddddd']

arquivo.writelines([i + '\n' for i in informacoes])

arquivo.close()
