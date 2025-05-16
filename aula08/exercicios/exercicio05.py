from datetime import datetime


def tempo_restante_fim_modulo():
    agora = datetime.now()
    fim_modulo = datetime(2024, 12, 2, 22, 0, 0)
    restante = fim_modulo - agora

    print(f"Tempo restante para o fim do módulo: {restante.days} dias e {restante.seconds // 3600} horas")

tempo_restante_fim_modulo()
