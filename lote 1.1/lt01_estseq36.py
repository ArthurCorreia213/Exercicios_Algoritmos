#Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N! 

#Arthur Correia

def fatorial(num):
    resultado=1
    for numero in range(num,1,-1):
        resultado*=numero
    return resultado

numero = int(input("Digite um número inteiro: "))
resultado=1

for num in range(1,numero+1):
    resultado+=1/(fatorial(num))
    
print(resultado)