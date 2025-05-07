'''
Dada a lista a seguir, usando pack/unpacking, atribua o primeiro elemento a uma variável
`primeiro`, o último elemento a uma variável `ultimo`, e os demais elementos a uma lista `meio`.

Exiba todos os elementos em prints separados. No print da lista `meio`, os elementos devem ser
separados por ponto e vírgula `;`.

`nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"]`
'''


nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo"]

primeiro, *meio, ultimo = nomes

print(primeiro)
print(meio)
print(ultimo)
