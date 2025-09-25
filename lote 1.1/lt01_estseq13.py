#Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias 
#durará esse alimento sabendo que a pessoa consome 50g ao dia.
#Arthur Correia

quantidade_de_alimento = float(input("Digite a quantidade de alimento em quilos: "))
print(f"Uma pessoa consumindo 50g por dia levará {(quantidade_de_alimento)*1000/50:.2f} dias para consumir essa quantidade de alimentos")