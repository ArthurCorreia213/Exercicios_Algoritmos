#Receba 2 numeros diferentes. calcule se o maior é multiplo do menor
#Arthur Correia

def checar_se_multiplos(valor1, valor2):
    if valor2>valor1:
        if valor2%valor1==0:
            print(f"{valor2} é multiplo de {valor1}")
        else:
            print(f"{valor2} não é multiplo de {valor1}")

    if valor1>valor2:
        if valor1%valor2==0:
            print(f"{valor1} é multiplo de {valor2}")
        else:
            print(f"{valor1} não é multiplo de {valor2}")

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

checar_se_multiplos(num1, num2)