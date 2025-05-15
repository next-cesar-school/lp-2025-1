def calcular_divisao():
    try:
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))
        resultado = numerador / denominador
    except ValueError:
        print("Erro: Você deve digitar um número válido.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operação finalizada.")

calcular_divisao()
