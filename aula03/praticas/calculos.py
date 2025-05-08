def velocidade(distancia=100, tempo=2):
    print(f'Velocidade = {distancia/tempo} Km/h')

velocidade(150, 2)                  # posicional

velocidade(tempo=2, distancia=150)  # nomeado

'''dist = float(input('Insira a distância em kilômetros: '))
temp = float(input('Insira a duração em horas: '))

velocidade(dist, temp)
velocidade(tempo=temp, distancia=dist)'''

velocidade()
