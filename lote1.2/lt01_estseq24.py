#Receba um valor, mostre se ele é divisivel por 2 e/ou 3
#Arthur Correia

def checar_divisibilidade(valor):
    if valor%2==0:
        print(f"{valor} é divisível por 2")
    else:
        print(f"{valor} não é divisível por 2")

    if valor%3==0:
        print(f"{valor} é divisível por 3")
    else:
        print(f"{valor} não é divisível por 3")

num = int(input("Digite um valor: "))

checar_divisibilidade(num)