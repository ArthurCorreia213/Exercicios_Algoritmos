#Receba o númer de voltas, tamanho do circuito e a duração. Calcule a velocidade média em km/h

voltas = int(input("Digite o número de voltas percorridas: "))
tamanho = int(input("Digite o tamanho do circuito em metros: "))/1000
duracao = float(input("Digite a duração do circuito em minutos: "))/60

kmh = ((tamanho/duracao)*voltas)

print(f"{kmh:.2f}Km/h")