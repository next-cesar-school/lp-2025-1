def somaImposto(taxa_imposto,custo):
    novo_custo = custo * ((taxa_imposto/100)+1)
    return novo_custo

custo = float(input('Informe o valor do produto: '))
taxa_imposto = int(input('Informe a taxa Imposto em porcentagem: '))
novo_custo = somaImposto(taxa_imposto, custo)
print(novo_custo)
