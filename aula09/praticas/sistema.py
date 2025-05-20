from gerenciador_arquivos.ler_arquivo import ler
from gerenciador_arquivos.escrever_arquivo import escrever

conteudo = ler('aula09/praticas/exemplo.txt')
conteudo = conteudo.upper()
escrever('aula09/praticas/exemplo_novo.txt', conteudo)
