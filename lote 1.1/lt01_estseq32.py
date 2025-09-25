#Receba um número inteiro. Calcule e mostre o seu fatorial. 
#Arthur Correia

numero = int(input("Digite um número inteiro: 0"))
resultado = 1
for num in range(numero,1,-1):
    resultado*=num
print(f"O fatorial de {numero} é {resultado}")