# NExT 2025.1

## **Lógica de Programação** com Python

![CESAR School](/cesar_school.png)

## Aula 08 - Módulos

### Na aula de hoje

- O que são módulos;
- Como utilizar alguns dos principais módulos nativos do Python;
- Boas práticas no uso de módulos.

------------------

## Módulos

À medida que nossos programas se tornam maiores e mais complexos, organizar o código é essencial. Em Python, usamos **módulos** e **pacotes** para dividir programas em partes menores e reutilizáveis. Além disso, Python oferece uma ampla gama de módulos nativos que já resolvem muitos problemas comuns, como manipulação de arquivos, cálculos matemáticos, operações com datas e tempo, entre outros.

## 🧰 Módulo

Por mais que a linguagem Python venha com uma série de recursos que otimizam bastante o tempo de desenvolvimento dos algoritmos, ela não é completa. Há uma série de cálculos, estruturas de dados e recursos para tratar com formatos de arquivos específicos que não está disponível nativamente na linguagem.

Para evitar o esforço de "reinventar a roda", podemos importar tais recursos desenvolvidos por outros programadores como **módulos**.

Um módulo é um arquivo Python que contém definições e implementações de funções, _classes_ e variáveis. O Python já vem com uma grande quantidade de módulos prontos para uso, conhecidos como **biblioteca padrão**.

### Importando módulos

Quando instalamos o Python, ele vem acompanhado de dezenas de modulos. A lista completa pode ser encontrada [aqui](https://docs.python.org/3/py-modindex.html).

Destacamos alguns:

- [calendar](https://docs.python.org/3/library/calendar.html#module-calendar)
- [copy](https://docs.python.org/3/library/copy.html#module-copy)
- [csv](https://docs.python.org/3/library/csv.html#module-csv)
- [datetime](https://docs.python.org/3/library/datetime.html#module-datetime)
- [json](https://docs.python.org/3/library/json.html#module-json)
- [statistics](https://docs.python.org/3/library/statistics.html#module-statistics)

Para adicionar um módulo, basta usar o comando `import` seguido no nome do módulo.

Existem três formas principais de importar módulos:

1. **Importar o módulo inteiro:**

    ```python
    import math


    print(math.sqrt(16))  # Saída: 4.0
    ```

2. **Importar elementos específicos do módulo:**

    ```python
    from math import sqrt, pi


    print(sqrt(25))  # Saída: 5.0
    print(pi)        # Saída: 3.141592653589793
    ```

3. **Importar com alias (apelido):**

    ```python
    import math as m


    print(m.sqrt(9))  # Saída: 3.0
    ```

## Principais Módulos Nativos do Python

### 🔢 `math`

Módulo matemático.

Fornece recursos matemáticos baseados na linguagem C, como cálculos trigonométricos, fatoriais e exponenciais.. Mais detalhes [aqui](https://docs.python.org/3/library/math.html#module-math).

```python
import math


print(math.sqrt(16))      # Raiz quadrada: 4.0
print(math.factorial(5))  # Fatorial: 120
print(math.pi)            # Valor de pi: 3.141592653589793
print(math.pow(2, 3))     # Potenciação: 2³
print(math.ceil(1.1))     # Arredondamento para cima
print(math.floor(1.9))    # Arredondamento para baixo
```

### 🔀 `random`

O módulo `random` permite trabalhar com geração de números pseudo-aleatórios e escolha de elementos de coleções.

Mais detalhes [aqui](https://docs.python.org/3/library/random.html#module-random).

Exemplo de uso:

```python
import random


print(random.randint(1, 10))             # Número aleatório entre 1 e 10
print(random.choice(['a', 'b', 'c']))    # Escolhe aleatoriamente um elemento da lista
print(random.sample(range(100), 5))      # Escolhe 5 números aleatórios sem repetição

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)                     # Embaralha toda a lista (não retorna nada)
```

### 📅 `datetime`

O módulo `datetime` é usado para trabalhar com datas e horas.

Exemplo de uso:

```python
from datetime import datetime, timedelta


agora = datetime.now()
print(agora)  # Data e hora atual

amanha = agora + timedelta(days=1)
print(amanha)  # Data e hora de amanhã

data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(data_formatada)  # Exibe data formatada
```

### 💻 `os`

O módulo `os` permite interagir com o sistema operacional, como navegar em diretórios, criar pastas e acessar variáveis de ambiente.

Mais detalhes [aqui](https://docs.python.org/3/library/os.html#module-os).

> **⚠️ CUIDADO!**
>
> Como esse módulo manipula os arquivos e pastas no seu computador, cuidado para não deletar ou alterar algo por acidente!

```python
import os


print(os.getcwd())          # Diretório atual
os.mkdir("nova_pasta")      # Cria uma pasta chamada 'nova_pasta'
os.rmdir("nova_pasta")      # ⚠️ Remove a pasta chamada 'nova_pasta'
os.path.exists('teste.txt') # Vefifica se um caminho existe
```

### 🎲 `csv`

O módulo csv facilita a leitura e escrita de arquivos no formato CSV (Comma-Separated Values), amplamente utilizado para troca de dados entre sistemas.

#### Leitura de arquivos CSV

Para ler um arquivo CSV, usamos `csv.reader`, que retorna as linhas como listas.

Exemplo de leitura:

```python
import csv


with open("dados.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
```

#### Escrita em arquivos CSV

Para escrever em um arquivo CSV, usamos `csv.writer`, que permite adicionar linhas de dados.

Exemplo de escrita:

```python
import csv


dados = [
    ["Nome", "Idade", "Cidade"],
    ["Frederico", 30, "Recife"],
    ["Ana", 25, "São Paulo"],
    ["Beto", 35, "Olinda"]
]

with open("saida.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)
```

#### Usando `DictReader` e `DictWriter`

Podemos ler e escrever arquivos CSV como dicionários, onde cada linha é um dicionário com as colunas como chaves.

Exemplo com `DictReader`:

```python
import csv


with open("dados.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)  # Cada linha é um dicionário
```

Exemplo com `DictWriter`:

```python
import csv


dados = [
    {"Nome": "Freferico", "Idade": 30, "Cidade": "Recife"},
    {"Nome": "Ana", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Beto", "Idade": 35, "Cidade": "Olinda"}
]

with open("saida.csv", "w", newline="") as arquivo:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()  # Escreve o cabeçalho
    escritor.writerows(dados)
```

## Boas Práticas ao Usar Módulos

1. Importe apenas o necessário:

    Evite importar módulos ou funções que não serão usados.

2. Organize as importações:

    Coloque todas as importações no início do arquivo.

3. Use nomes descritivos:

    Evite usar alias que dificultem a leitura do código.

4. Aproveite a biblioteca padrão:

    Antes de criar suas próprias funções, verifique se já existe um módulo nativo que resolva o problema.

## Bônus - Easter Eggs do Python

Existem alguns pequenos segredos escondidos na própria linguagem que revelam o bom-humor da comunidade e, de quebra, ajudam a fixar conceitos sobre módulos e importação.

1. `import this` – O Zen of Python

    Quando você digita `import this` no interpretador, o Python carrega um poema com 19 princípios de design que norteiam a linguagem.

    Não tem finalidade prática direta no código, mas é um lembrete elegante dos valores de legibilidade e simplicidade que buscamos ao programar. Ótimo para abrir discussões sobre boas práticas antes de aprofundar em PEP 8 (nas próximas aulas).

2. `from __future__ import braces` – {} Chaves em Python

    O módulo `__future__` é usado oficialmente para habilitar recursos que chegarão em versões futuras (ex.: `from __future__ import annotations`).

    Este módulo promete ativar suporte a {} como delimitadores de bloco (à moda de C/Java).

3. (Extra) `import antigravity`

## 🧱 Exercícios Fundamentais

1. A partir do valor do raio informado pelo usuário, calcule a area da circunferência utilizando funções e π (pi) do modulo `math`.

2. Use o módulo `math` para calcular e exibir:
    - A raiz quadrada de 144;
    - O valor do cosseno de 45° (em radianos);
    - O valor de `e` elevado a 2.

3. Crie uma função que atue como um simulador de dado 🎲 (valor entre 1 e 6). Se o valor for igual a 6, exiba a mensagem: "Dano Crítico!".

4. Use o módulo `random` para criar um jogo onde o programa escolhe um número aleatório entre 0 e 10 e o usuário deve tentar adivinhar o valor. Quando a pessoa acertar, deve ser apresentado uma pontuação (se acertar de primeira, 10 pontos, na segunda tentativa, 9 pontos...)

5. Use o módulo `datetime` para implementar uma função que retorne quanto tempo falta para o final deste módulo:
    - Exiba o tempo seguindo o formato: `Tempo restante para o fim do módulo: XX dias e YY horas`;

## 🤿 Exercícios de Aprofundamento

6. Use o módulo os para criar uma estrutura de pastas e arquivos:
    - Uma pasta chamada "projeto" com dois subdiretórios: "src" e "docs";
    - Um arquivo vazio chamado "README.md" dentro de "docs".

7. Use o módulo `csv` para refazer as questões do desafio `PyFinanceiro` e `PyVotação`, da aula de arquivos. Altere a extensão dos arquivos de `.txt` para `.csv`.
