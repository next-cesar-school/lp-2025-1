# NExT 2025.1

## **Lógica de Programação** com Python

![CESAR School](/cesar_school.png)

## Aula 04 - Noções de Programação Funcional

### Na aula de hoje

- O que é Programação Funcional
- Funções Lambda
- Map, Filter e Reduce

------------------

## Programação Funcional no Python

A programação funcional é um paradigma de programação que trata a computação como a avaliação de funções matemáticas e evita estados e dados mutáveis. Python, embora seja uma linguagem multiparadigma, oferece suporte a conceitos de programação funcional, como funções de primeira classe, funções anônimas (**lambda**), e funções de ordem superior como `map`, `filter` e `reduce`.

Na aula de hoje, exploraremos esses conceitos fundamentais e como utilizá-los em Python para escrever código mais conciso e expressivo.

## λ Funções Lambda

Em Python, uma função **lambda** é uma função anônima, ou seja, uma função sem declaração de nome. Elas são úteis quando precisamos de uma função **simples e pequena** para ser usada uma única vez, geralmente como argumento para outra função.

### Sintaxe das funções lambda

A sintaxe básica de uma função lambda é:

```python
lambda argumentos: expressão
```

- `lambda`: palavra-chave que indica que uma função lambda está sendo declarada.
- `argumentos`: uma lista separada por vírgulas de argumentos da função.
- `expressão`: uma expressão que é avaliada e retornada pela função.

Exemplo simples:

```python
soma = lambda a, b: a + b
print(soma(2, 3))
```

### Exemplos de uso

#### Exemplo 1: Ordenação personalizada

```python
lista = [[1, 2], [3, 1], [5, 0]]
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)
```

#### Exemplo 2: Função dentro de outra função

```python
def multiplicador(n):
    return lambda x: x * n

duplica = multiplicador(2)
print(duplica(5))
```

## Função `map`

A função `map` aplica uma função a todos os itens de um iterável (como uma lista) e retorna um objeto map (um iterador) com os resultados.

### Sintaxe e uso da função `map`

```python
map(função, iteravel, ...)
```

- `função`: a função a ser aplicada aos itens.
- `iterável`: um ou mais iteráveis.

### Exemplos práticos

#### Exemplo 1: Converter entradas

```python
numeros = list(map(int, input().split()))

print(numeros)
```

#### Exemplo 2: Converter uma lista de números em suas potências ao quadrado

```python
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)
```

#### Exemplo 3: Somar elementos de duas listas

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
soma_listas = list(map(lambda x, y: x + y, lista1, lista2))
print(soma_listas)  # Saída: [5, 7, 9]
```

#### Exemplo 4: Manular strings em uma lista

```python
palavras = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']

palavras = list(map(lambda d: d.upper(), palavras))

print(palavras)
```

#### Exemplo 5: Ordenação personalizada

```python
numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros2 = [9, 8, 7, 6, 5]

print(list(map(lambda n1, n2: n1 + n2, numeros1, numeros2)))
```

## Função `filter`

A função `filter` constrói um iterador a partir dos elementos de um iterável para os quais a função retorna `True`.

### Sintaxe e uso da função `filter`

```python
filter(função, iteravel)
```

- `função`: uma função que retorna um valor booleano.
- `iterável`: o iterável a ser filtrado.

### Exemplos práticos

#### Exemplo 1: Filtrar números pares de uma lista

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
```

#### Exemplo 2: Filtrar palavras com mais de 3 letras

```python
palavras = ["sol", "lua", "estrelas", "mar", "céu"]
longas = list(filter(lambda x: len(x) > 3, palavras))
print(longas)
```

## Função `reduce`

A função `reduce` aplica uma função de dois argumentos cumulativamente aos itens de um iterável, reduzindo o iterável a um único valor.

> Nota: Em Python 3, `reduce` foi movida para o módulo `functools`.

### Sintaxe e uso da função `reduce`

```python
from functools import reduce

reduce(função, iteravel[, valor_inicial])
```

- `função`: função de dois argumentos.
- `iterável`: o iterável cujos itens serão reduzidos.
- `valor_inicial` (opcional): valor inicial que precede os itens do iterável.

### Exemplos práticos

#### Exemplo 1: Somar todos os números de uma lista

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)
```

#### Exemplo 2: Encontrar o máximo em uma lista

```python
from functools import reduce

numeros = [5, 8, 2, 1, 9, 3]
maior = reduce(lambda x, y: x if x > y else y, numeros)
print(maior)
```

## 🧱 Exercícios Fundamentais

1. Dobrar números pares

    Dada a lista `numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, use filter e map para criar uma nova lista contendo o dobro dos números pares.

2. Filtrar palavras que começam com uma letra específica

    Dada a lista `palavras = ["python", "java", "javascript", "c++", "c#", "ruby", "go"]`, use filter para obter as palavras que começam com a letra `"j"`.

3. Produto de uma lista de números

    Utilize a função `reduce` para calcular o produto (multiplicação) de todos os números na lista `numeros = [1, 2, 3, 4, 5]`.

4. Listar os comprimentos das palavras

    Dada a lista `palavras = ["maçã", "banana", "cereja", "damasco"]`, use map para criar uma lista com os comprimentos de cada palavra.

5. Extrair os dígitos de uma string

    Dada a string `texto = "Eu tenho 2 maçãs e 3 laranjas."`, use filter para extrair os dígitos e formar uma lista `['2', '3']`.

6. Combinar `map` e `reduce`

    Use `map` para obter o quadrado dos números na lista `numeros = [1, 2, 3, 4]` e, em seguida, use `reduce` para somar esses quadrados.

7. Maior palavra em uma lista

    Utilize `reduce` para encontrar a palavra mais longa na lista `palavras = ["sol", "montanha", "mar", "universo"]`.

8. Converter temperaturas

    Dada a lista de temperaturas em Celsius `temperaturas_c = [0, 20, 35, 100]`, use `map` para convertê-las em Fahrenheit.

    Fórmula: $F = C * 9/5 + 32 $

9. Filtrar números primos

    Dada a lista `numeros = list(range(2, 20))`, escreva uma _função lambda_ para verificar se um número é primo e use `filter` para obter todos os números primos da lista.

10. Contar ocorrências de uma letra

    Dada a lista `palavras = ["banana", "abacate", "morango", "abacaxi"]`, use `map` para contar quantas vezes a letra `"a"` aparece em cada palavra, resultando em uma lista de contagens.
