import os


def criar_estrutura_projeto():
    os.makedirs("projeto/src", exist_ok=True)
    os.makedirs("projeto/docs", exist_ok=True)
    
    caminho_readme = os.path.join("projeto", "docs", "README.md")
    with open(caminho_readme, "w") as arquivo:
        pass  # Cria o arquivo vazio

    print("Estrutura de pastas e arquivo README.md criada com sucesso!")

criar_estrutura_projeto()
