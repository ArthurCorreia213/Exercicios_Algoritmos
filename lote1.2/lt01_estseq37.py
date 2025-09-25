#Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu 
#N’nésimo termo
#Arthur Correia

def fib(numero):
    n1 = 0
    n2 = 0

    for i in range(numero):
        soma = n1+n2
        if soma == 0:
            soma = 1
            n1=soma
        else:
            if n1>=n2:
                n2 = soma
            else:
                n1 = soma
        print(soma)

numero = int(input("Digite um número: "))

fib(numero)