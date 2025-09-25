#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
#Arthur Correia

numero = int(input("Digite um número inteiro: "))
resultado=1

for num in range(2,numero+1):
    resultado+=1/num

print(resultado)