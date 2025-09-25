# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e 
# mostre o resultado da somatória dos números ímpares entre esses valores. 

#Arthur Correia

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = 0

if num1>num2:
    for numero in range(num2+1, num1):
        if numero%2!=0:
            resultado+=numero
    print(resultado)
elif num2>num1:
    for numero in range(num1+1, num2):
        if numero%2!=0:
            resultado+=numero
    print(resultado)
else:
    print("Os números são iguais")