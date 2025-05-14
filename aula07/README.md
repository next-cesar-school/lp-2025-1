# NExT 2025.1

## **Lógica de Programação** com Python

![CESAR School](/cesar_school.png)

## Aula 07 - Tratamento de Exceções

### Na aula de hoje

- Exceções
- `try`, `except`, `else`, `finally`
- Boas práticas no tratamento de exceções

------------------

## Tratamento de Exceções

O tratamento de exceções é uma técnica fundamental para tornar os programas mais **robustos** e capazes de lidar com erros de maneira controlada. Em Python, as exceções são eventos que **interrompem o fluxo normal do programa**, mas que podem ser tratadas para evitar falhas inesperadas.

As exceções em Python **ocorrem durante a execução do programa** e que podem interromper o fluxo normal do código. Alguns exemplos de situações comuns que geram exceções:

- Divisão por zero: `ZeroDivisionError`
- Índice fora do intervalo: `IndexError`
- Tipo inválido: `TypeError`
- Arquivo inexistente: `FileNotFoundError`

Exemplo:

```python
numeros = [1, 2, 3]
print(numeros[5])  # Lança IndexError
```

## Lidando com Exceções: `try` e `except`

O bloco `try` permite testar um trecho de código que pode gerar uma exceção. O bloco `except` define o que fazer quando a exceção ocorre.

Exemplo:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')
```

## Capturando múltiplas exceções

É possível tratar várias exceções de diferentes formas:

```python
try:
    numero = int(input('Digite um número: '))
    resultado = 10 / numero
except ValueError:
    print('Erro: Você deve digitar um número.')
except ZeroDivisionError:
    print('Erro: Não é possível dividir por zero.')
```

Ou ainda, capturando várias exceções para um tratamento único:

```python
try:
    numero = int(input('Digite um número: '))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError):
    print('Erro: Algo de errado não está certo')
```

## Blocos `else` e `finally`

- `else`: Executado se nenhuma exceção ocorrer;
- `finally`: Executado sempre, independentemente de exceções.

```python
try:
    arquivo = open('dados.txt', 'r')
    conteudo = arquivo.read()
except FileNotFoundError:
    print('Erro: Arquivo não encontrado.')
else:
    print('Arquivo lido com sucesso!')
finally:
    print('Encerrando operação.')
```

## Boas Práticas no Tratamento de Exceções

1. Trate apenas as exceções esperadas.

    Evite capturar exceções genéricas com `except Exception`.

2. Seja específico.

    Capture exceções específicas para um tratamento mais claro.

3. Use `finally` para liberar recursos.

    Feche arquivos ou conexões no bloco `finally`.

4. Não esconda erros.

    Sempre informe o que aconteceu e como o usuário pode corrigir.

## 🐝 Exercícios Beecrowd

[2653 - Dijkstra](https://www.beecrowd.com.br/judge/pt/problems/view/2653)

[1068 - Balanço de Parênteses I](https://judge.beecrowd.com/pt/problems/view/1068)

[3038 - Carta de Natal Criptografada](https://judge.beecrowd.com/pt/problems/view/3038)

[1467 - Zerinho ou Um](https://judge.beecrowd.com/pt/problems/view/1467)

[1789 - A Corrida de Lesmas](https://judge.beecrowd.com/pt/problems/view/1789)

## 🧱 Exercícios Fundamentais

1. Escreva um programa que leia dois números do usuário e calcule a divisão entre eles. Use exceções para tratar:
    - Erros de entrada (`ValueError`);
    - Divisão por zero (`ZeroDivisionError`).

2. Implemente uma função que abra um arquivo para leitura, seguindo informações inseridas pelo usuário, e exiba seu conteúdo. Trate o erro de arquivo não encontrado (`FileNotFoundError`).

3. Crie uma função que receba um dicionário e uma chave, retornando o valor correspondente. Trate o erro de chave inexistente (`KeyError`).
