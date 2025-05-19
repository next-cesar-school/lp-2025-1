# NExT 2025.1

## **Lógica de Programação** com Python

![CESAR School](/cesar_school.png)

## Aula 09 - Criando Seus Próprios Módulos

### Na aula de hoje

- Benefícios da modularidade;
- Como criar módulos e pacotes;
- Boas práticas na organização de projetos Python;
- Projetos para praticar a criação de módulos e pacotes.

------------------

## 🧰 Módulos

Um **módulo** é um arquivo Python (`.py`) que contém definições de funções, _classes_ e variáveis que podem ser reutilizadas em outros arquivos Python.

### Benefícios dos módulos

- Reutilização de código em diferentes projetos;
- Redução da duplicação de código;
- Facilitação na manutenção e organização.

### Criando um módulo

1. Crie um arquivo Python com o nome `meu_modulo.py`:

    ```python
    # Arquivo: meu_modulo.py
    def saudacao(nome):
        return f"Olá, {nome}! Bem-vindo ao NExT."
    ```

2. Use o módulo em outro arquivo:

    ```python
    # Arquivo: exemplo.py
    import meu_modulo


    print(meu_modulo.saudacao("Erick"))
    ```

## 📦 Pacotes

Em casos onde vários módulos fazem parte de uma mesma solução, pode ser interessantes agrupa-los em pacotes (packages).

Um pacote é uma coleção de módulos organizados em um diretório. Ele contém um arquivo especial `__init__.py` que pode estar vazio ou conter código de inicialização. Quando fazemos um `import`, é possível importar todos os módulos de um pacote, ou apenas alguns específicos.

## Estrutura de um pacote

Um pacote chamado `calculadora` com dois módulos (`basico.py` e `cientifico.py`) poderia ter a seguinte estrutura:

```txt
calculadora/
    __init__.py
    basico.py
    cientifico.py
```

### Exemplo de Pacote

1. `basico.py`:

    ```python
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b
    ```

2. `cientifico.py`:

    ```python
    def raiz_quadrada(x):
        return x ** 0.5

    def potencia(base, expoente):
        return base ** expoente
    ```

3. Uso do pacote em um programa:

    ```python
    from calculadora.basico import somar
    from calculadora.cientifico import raiz_quadrada

    print(somar(2, 3))           # Saída: 5
    print(raiz_quadrada(16))     # Saída: 4.0
    ```

## Benefícios da Modularidade

- **Organização**: Divide o código em partes menores e mais gerenciáveis.
- **Reutilização**: Permite usar o mesmo código em diferentes projetos.
- **Testabilidade**: Módulos menores são mais fáceis de testar e depurar.
- **Manutenção**: Atualizações são localizadas, reduzindo o impacto em outras partes do sistema.

## Boas Práticas na Criação de Módulos e Pacotes

1. Use nomes descritivos:
    - Nomeie módulos e pacotes de forma clara e concisa;
    - Evite abreviações confusas.

2. Evite importações circulares:
    - Não crie dependências entre módulos que se importam mutuamente.

3. Organize arquivos relacionados:
    - Agrupe módulos com funções semelhantes em pacotes.

4. Use o arquivo `__init__.py`:
    - Utilize-o para inicializar pacotes e expor apenas o necessário.

5. Documente seus módulos:
    - Inclua docstrings para descrever a finalidade de cada módulo e função.

## 🔨 Projetos Fundamentais

## 1. Criando um Pacote de Utilidades

Pacote com recursos genéricos de utilidades.

1. Estrutura do pacote:

    ```txt
    utilidades/
        __init__.py
        strings.py
        numeros.py
    ```

2. `strings.py`:
    - Funções:
        - `contar_vogais(texto)`: Conta o número de vogais em uma string.
        - `inverter(texto)`: Retorna o texto invertido.

3. `numeros.py`:
    - Funções:
        - `eh_primo(n)`: Verifica se um número é primo.
        - `fatorial(n)`: Calcula o fatorial de um número.

4. Teste o pacote criando um programa que utiliza as funções.

## 2. Sistema de Gerenciamento de Estoque

Sistema capaz de adicionar e remover produtos de um estoque. Todos os dados devem ser salvos em arquivo.

1. Estrutura do pacote:

    ```txt
    estoque/
        __init__.py
        produtos.py
        vendas.py
    ```

2. `produtos.py`:
    - Funções:
        - `adicionar_produto(nome, quantidade, preco)`: Adiciona um produto ao estoque.
        - `remover_produto(nome)`: Remove um produto do estoque.
        - `listar_produtos()`: Exibe todos os produtos.

3. `vendas.py`:
    - Funções:
        - `registrar_venda(produto, quantidade)`: Atualiza o estoque após uma venda.
        - `calcular_total_vendas()`: Calcula o total de vendas realizadas.

4. Crie um programa que utilize o pacote para gerenciar um estoque fictício..
