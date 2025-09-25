#Calcule a quantidade de litros gastos em uma viagem, sabendo que o 
#automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média. 
#Arthur Correia

tempo = float(input("Digite o número de horas viajadas: "))
velocidade_media = float(input("Digite a velocidade média da viagem (km/h): "))

distancia_viajada = tempo*velocidade_media

print(f"Um veículo que faz 12km/L gasta {distancia_viajada/12:.2f}litros em uma viagem de {distancia_viajada}km")