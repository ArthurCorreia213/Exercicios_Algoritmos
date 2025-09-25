#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor
#Arthur Correia
def maior_menor(valor1, valor2):
    if valor1>valor2:
        print(valor1-valor2)
    else:
        print(valor2-valor1)

num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))

maior_menor(num1,num2)