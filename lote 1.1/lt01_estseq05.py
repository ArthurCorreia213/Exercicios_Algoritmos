#Receba os coeficientes A, B e C de uma equação do 2º grau 
#(AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a 
#equação possue2 raízes). 

#Arthur Correia

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b**2)-(4*a)*c

x1 = (-b+(delta**0.5))/2*a

x2 = (-b-(delta**0.5))/2*a

print(delta)
print(x1)
print(x2)