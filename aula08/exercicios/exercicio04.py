from random import randint


def jogo_adivinhar_numero():
    numero_aleatorio = randint(0, 10)
    tentativas = 0
    pontos = 10

    while True:
        tentativa = int(input("Adivinhe o número entre 0 e 10: "))
        tentativas += 1

        if tentativa == numero_aleatorio:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativa(s). Pontuação: {pontos}")
            break
        else:
            pontos -= 1
            print("Errado, tente novamente.")

jogo_adivinhar_numero()
