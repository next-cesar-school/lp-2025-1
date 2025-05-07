# NExT 2025.1

## **Lógica de Programação** com Python

![CESAR School](/cesar_school.png)

## Aula 03 - Funções

### Na aula de hoje

- Funções

------------------

## ⚙️ Funções

Desde que começamos a programar em Python temos descoberto várias funções da linguagem:

- `print()`
- `len()`
- `del()`

e também várias funções de tipos específicos de dados:

- `str.lower()`
- `lista.append()`

Essas funções são implementadas pela própria linguagem e executam tarefas específicas. Graças a elas economizamos muito tempo, tendo em vista que não só já foram implementadas, mas também foram testadas e validadas por toda a comunidade que usa a Python.

Nesta aula aprenderemos a escrever nossas próprias funções!

### Definição de função

Funções são definidas em Python usando o comando `def()`. Dois pontos `:` são usados para indicar o bloco da função.

```python
def nome_funcao():
  pass
```

Para executar a função, basta chamá-la por sua **assinatura**:

```python
nome_funcao()
```

### Parâmetros

Várias funções que conhecemos recebem parâmetros. Também podemos fazer isso da seguinte forma:

```python
def nome_funcao(param):
  pass
```

> 💡 Geralmente usamos as experssões **parâmetros** e **argumentos** como sinônimos, mas, tecnicamente, podem ser usados em contexto diferentes:
>
> - Parâmetro é o variável listada na definição da função;
> - Argumento é o valor que é enviado para a funçõa quando ela é chamada.

### Argumentos posicionais e nomeados

- **Posicional**: Quando são passados na mesma ordem dos parâmetros
- **Nomeados**: Um par nome-valor (`arg=valor`) passados para a função

```python
# V = d/t
def velocidade(distancia, tempo):
  print(distancia/tempo)
```

### Valores predefinidos

Quando uma determinada função recebe sempre os mesmos parâmetros, para facilitar seu uso, podemos definir valores *default*.

Esse tipo de técnica é usada no `print` que tem 4 parâmetros opcionais previamente definidos:

```python
 print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

> 💡 *Mais detalhes sobre o print [aqui](https://docs.python.org/3/library/functions.html#print).*

> ⚠️ Os valores *default* devem ser sempre os últimos!

### Quantidade arbitrária de parâmetros

Em Python é possível deixar flexível a quantidade de parâmetros que uma função pode receber, como acontece com o `print()`:

```python
print(var1)
print(var1, var2, var3)
```

Para esses casos, basta adicionar um `*` antes do nome da variável.

```python
def func(*valores):
  pass
```

> ⚠️ Caso seja necessário receber mais valores, os parâmetros seguintes precisam ter, obrigatoriamente, valores *default*.

## ↩️ Retornando Valores

Para que uma função possa devolver um valor para sua chamada, usamos a palavra reservada `return`.

> ⚠️ Depois que o comando `return` é alcançado, a função é finalizada. Qualquer código após o `return` é inalcançável.

## Função com funções

Funções internas ou funções aninhadas, são funções definidas dentro de outras funções.

Podem ser usadas para esconder um recurso de acesso externo ou para criação de funções auxiliares que só funcionam em determinado contexto.

Mais sobre Inner Functions [aqui](https://realpython.com/inner-functions-what-are-they-good-for/).

## ♾️ Funções recursivas

É chamada de **função recursiva** aquela que faz uma chamada para ela mesma. Seu uso é recomendado em casos onde sua implementação é mais eficiente ou mais simples do que outras técnicas.

> ⚠️ Assim como ocorre com uma estrutura de repetição, é necessário definir uma condiçõa de saída
>
> ⚠️ Geralmente podem ser subistituídas por estruturas de repetição.

## 🐝 Beecrowd

- [3475 - Conversor](https://judge.beecrowd.com/pt/problems/view/3475)
- [1099 - Soma de Ímpares Consecutivos II](https://judge.beecrowd.com/pt/problems/view/1099)
- [1151 - Fibonacci Fácil](https://judge.beecrowd.com/pt/problems/view/1151)

## 🧱 Exercícios Fundamentais

1. Crie um programa que receba um valor inteiro e avalie se ele é positivo ou negativo. Essa avaliação deve ocorrer dentro de uma função que retorna um valor booleano.

2. Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os valores multiplicados por um valor inserido pelo usuário.

3. Crie um programa que possua uma lista de nomes. Peça que o usuário insira um nome que será buscado nesta lista. A busca deve ser implementada em uma função que retorna os valores lógicos verdadeiro, caso o nome seja encontrado na lista ou falso, caso contrário.

4. Implemente um programa que possa receber do usuário a temperatura em graus Celsius ou Fahrenheit. Antes de receber a temperatura, pergunte ao usuário se ele deseja inserir em Celsius ou em Fahrenheit. Se a entrada for em graus Celsius, o programa deverá retornar a temperatura em Fahrenheit. Se a entrada for em Fahrenheit, o programa deverá retornar a temperatura em Celsius.

    $ °C = 5 \times ((°F-32) / 9) $

    $ °F = (°C \times 9 / 5) + 32 $

5. Crie um programa que receba do usuário 5 números inteiros e os exiba na tela na ordem contrária a que foi inserido. A leitura dos números deve ser feita em uma função e a exibição dos valores em ordem contrária deve ocorrer em outra função.

6. Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os seus valores em ordem invertida.
Obs.: Sem usar `invert` ou o fatiador com passo `-1`.

## 🤿 Exercícios de Aprofundamento

⚠️ Alguns desses exercícios exigem conhecimentos ainda não apresentados no curso!

7. Faça um programa para imprimir:

    ```txt
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
    ```

8. Faça um programa para imprimir:

    ```txt
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
    ```

9. Faça uma função que receba um valor inteiro e positivo e calcule o seu fatorial.

10. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

11. Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”. Escreva um função que dado uma plavra verifique se ela é palindro.

12. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

💡 Pesquise sobre o módulo `random`
