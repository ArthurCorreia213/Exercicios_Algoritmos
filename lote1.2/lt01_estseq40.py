# Receba 2 números inteiros. Verifique e mostre todos os números primos 
# existentes entre eles.
#Arthur Correia

def checar_se_primo(num):
    if num == 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def primos_entre_numeros():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    while num1 < 0 or num2 < 0:
        print("Numeros negativos não são aceitos")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

    if num1>num2:   
        numeros = [i for i in range(num2, num1+1)]
    elif num2>num1:   
        numeros = [i for i in range(num1, num2+1)]
    else:
        print("Números iguais não são aceitos")
        numeros = []
        
    primos = []

    for numero in numeros:
        if checar_se_primo(numero):
            primos.append(numero)

    for numero in primos:
        print(numero)

    print(numeros)
    print(primos)

primos_entre_numeros()