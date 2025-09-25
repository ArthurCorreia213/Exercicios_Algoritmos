# Receba 2 números inteiros. Verifique e mostre todos os números primos 
# existentes entre eles.
#Arthur Correia

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1>num2:   
    numeros = [i for i in range(num1, num2+1)]
elif num2>num1:   
    numeros = [i for i in range(num2, num1+1)]
else:
    print("Números iguais não são aceitos")
    numeros = []
    
primos = []

for numero in numeros:
    contador =2 
    while contador < numero:
        if numero%contador == 0 or numero<2:
            break
        contador+=1
    
    else:
        if numero!=1:
            primos.append(numero)


for numero in primos:
    print(numero)