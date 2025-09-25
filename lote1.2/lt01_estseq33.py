#Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
#Arthur Correia

def calcular_serie():
    numero = int(input("Digite um número inteiro: "))
    resultado=1
    print('1',end='')
    for num in range(2,numero+1):
        resultado+=1/num
        print(f' + 1/{num}', end='')

    print('\n',resultado)

calcular_serie()