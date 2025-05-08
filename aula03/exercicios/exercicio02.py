def mult_lista(l, mult):
    for num in l:
      print(num * mult)


n_lista = int(input('Quantos números você deseja inserir? '))

l = []
for _ in range(n_lista):
    l.append(int(input('Insira um número: ')))

mult = int(input('Por qual valor vovê deseja multiplicar? '))

mult_lista(l, mult)
