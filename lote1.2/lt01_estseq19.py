#Receba 2 valores reais. Calcule e mostre o maior deles
#Arthur Correia
def identificar_maior(valor1, valor2):
    if valor1>valor2:
        print(f"O primeiro valor, {valor1}, é o maior dentre os digitados")
    else:
        print(f"O segundo valor, {valor2}, é o maior dentre os digitados")

num1 = float(input("Digite um valor real: "))
num2= float(input("Digite outro valor real: "))

identificar_maior(num1,num2)