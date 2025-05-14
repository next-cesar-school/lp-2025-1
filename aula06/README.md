# NExT 2025.1

## **Lógica de Programação** com Python

![CESAR School](/cesar_school.png)

## Aula 06 - Estruturas de Dados

### Na aula de hoje

- Tuple
- Set
- Dict

------------------

## Estruturas de Dados

Sempre que precisamos armazenar vários dados em uma única variável se faz necessário usar algum tipo de dado _container_. Em Python, os principais são:

- `list`;
- `tuple`;
- `set`;
- `dict`;

Cada containers, ou tipos de coleção, tem uma característica específica e um uso diferente. Nesta aula vamos conhecer um pouco mais sobre eles.

### 🪨 `tuple`

Ao usar listas, há bastante liberdade para alterar seus itens. Em determinadas situções, essas listas não deveriam ser alteradas. Para criar coleções de dados que não podem ser alterados, podemos usar `tuple` (tupla), em casos como:

- Dias da semana;
- Coordenadas de um prédio;
- Letras de um alfabeto.

```python
t = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
```

> #### Características

- Imutáveis;
- Ordenados/indexável;
- Permite elementos duplicados;
- Desempenho superior a listas.

> 💡 Obs.: _O acesso aos elementos de uma tupla é feito da mesma forma que com listas_

```python
# tuple -> Tópicos a explorar:
# - Criação de uma Tupla
# - Acesso aos elementos de uma Tupla
# - len()
# - tupla.index(item)
# - tupla.count(item)
# - Imutabilidade
```

### 💎 `set`

Tanto em **listas**, quanto em **tuplas**, é possível ter elementos repetidos:

```python
t = (0, 1, 1, 2, 3, 5)
l = [0, 1, 1, 2, 3, 5]
```

Quanto houver uma situação onde você não deva armazenar itens repetidos em uma coleção de dados, é possível usar um `set` (conjunto):

```python
s1 = set()
s.add(1)
s.add(2)
s.add(1)

s2 = {'bacon', 'banana', 'spam', 'ovos', 'spam', 'salsicha', 'spam'}
```

> #### Características

- Imutáveis (mas podem ser adicionados e removidos);
- Não Ordenados/não indexável;
- **Não Permite elementos repetidos**.

```python
# Tópicos a explorar:
# - criar um set
# - print(ingredientes[0]) # erro!
# - adicionar elementos
# - remover elementos
```

### 🔑 `dict`

Para criar estruturas de dados que são mapeados por valores (e não pelo indice, como nas listas) é possível usar um **dicionário**.

> **Chave** x **Valor**

Obs.: _O mapeamento é feito pela chave (e não pela ordem)_

Exemplos de uso prático:

- Dicionários;
- CEP;
- Tabela de valores;

```python
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
```

> #### Características

- Mutáveis;
- Ordenados/indexável;
- Permite valores duplicados (mas não a chave);
- Acesso aos valores rápido;
- Base para JSON e APIs.

```python
# Tópicos a explorar
# - Criando um dicionário
# - Acessando elementos de um dicionário
# - Adição de itens por atribuição
# - Adição de itens por update
# - Removendo itens
# - esvaziando um dicionário
```

### 🗝️ Alguns métodos úteis de dicionários

- `dict.keys()` - Apresenta todas as chaves do dicionário
- `dict.values()` - Apresenta todos os valores do dicionário
- `dict.items()` - `dict_keys()` + `dict_values()`
- `dict.get(chave, default)` - Retorna um elemento do dicionário. Se não encontrar, retorna o valor _default_.

```python
# Tópicos a explorar
# - adicioar valores + update()
# - get()
# - keys()
# - values()
# - items()
# - for
```

## 📋 Resumão

| Tipo  | Mutável | Ordenado | Indexável | Elementros Repetidos |
|-------| :-----: | :------: | :-------: | :-----------------:  |
|`list` |   ✅   |    ✅    |    ✅    |          ✅          |
|`tuple`|   ❌   |    ✅    |    ✅    |          ✅          |
| `set` |   ✅   |    ❌    |    ❌    |          ❌          |
|`dict` |   ✅   |    ✅    |    ✅*   |          ✅          |

## 🐝 Exercícios Beecrowd

[1050 - DDD](https://www.beecrowd.com.br/judge/pt/problems/view/1050)

[1168 - LED](https://www.beecrowd.com.br/judge/pt/problems/view/1168)

[1049 - Animal](https://judge.beecrowd.com/pt/problems/view/1049)

[1179 - Preenchimento de Vetor IV*](https://judge.beecrowd.com/pt/problems/view/1179)

[2653 - Dijkstra**](https://www.beecrowd.com.br/judge/pt/problems/view/2653)

\* questão sobre vetor, mas é uma boa oportunidade de usar função

\*\* Essa questão exige os conhecimentos da próxima aula

## 🧱 Exercícios Fundamentais

1. Dada a lista a seguir, crie uma nova lista onde cada um desses elementos aparece apenas uma única vez.

    ```python
    l = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
    ```

2. Crie um programa com duas funções. A primeira deve pedir um CEP e o endereço do usuário e armazena-lo em um dicionário. A segunda deve pesquisar um endereço, buscando pelo CEP informado.

🏆 Desafio: Armazene o dicionário em um arquivo.

## ✨ Bônus

Além dos tipos de coleção de dados clássicos apresentados na aula de hoje, Python possui alguns tipos utilitários presentes no módulo `collections`:

| Ferramenta | Para que serve  | Quando usar |
| ---------- | --------------- | ----------- |
| **`namedtuple`**  | Cria tuplas imutáveis com **campos nomeados**. Mantém o desempenho/memória de uma tupla, mas oferece acesso por atributo (`ponto.x`) e métodos úteis (`_replace`, `_asdict`). | Estruturas de dados leves que só agrupariam valores (ex.: coordenadas, result sets) sem precisar da “sobre-carga” de uma classe.                                                  |
| **`OrderedDict`** | Dicionário que preserva **ordem de inserção** _e_ expõe APIs extras como `move_to_end` e `popitem(last=False)`.                                                               | Quando a ordem faz parte da lógica (LRU cache, serialização com ordem definida). Obs.: desde Py 3.7 a ordem já é garantida em `dict`; o benefício hoje são os métodos adicionais. |
| **`ChainMap`**    | “Empilha” vários dicionários e os expõe como **um único mapeamento de leitura/escrita** (procura na sequência).                                                               | Construir escopos aninhados (config local → global → default), sobrescrever variáveis sem copiar grandes estruturas.                                                              |
| **`Counter`**     | Multiconjunto especializado em **contar ocorrências**. Suporta aritmética (`+`, `-`), `.most_common()` e atualização incremental.                                             | Estatísticas rápidas (frequência de palavras, contagem de itens vendidos) ou operações de bag/mochila.                                                                            |
| **`deque`**       | **Fila/stack** baseada em lista duplamente encadeada. Inserções e remoções `O(1)` em ambas as pontas, métodos `appendleft`, `popleft`, `rotate`, `maxlen`.                    | Implementar filas de tarefas, janelas deslizantes, algor. BFS, LRU simples — sem penar com `pop(0)` em listas normais.                                                            |
| **`defaultdict`** | Subclasse de `dict` que chama uma **factory** para criar valores-padrão ao acessar chave ausente.                                                                             | Contagens (`defaultdict(int)`), agrupamentos (`defaultdict(list/set)`), aninhamento fácil sem `if … in`.                                                                          |
