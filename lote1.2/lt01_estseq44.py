# Receba o número da base e do expoente. Calcule e mostre o valor da 
# potência
#Arthur Correia

def potenciacao(base, expoente):
    resultado_potencia = base**expoente
    print(f"O valor da potência é: {resultado_potencia}")

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

potenciacao(base, expoente)