# Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225 
#Arthur Correia

def calcular_serie():
    resultado = 1

    print('1', end='')
    for numero in range(2, 16):
        termo = numero / (numero ** 2)
        if numero % 2 == 0:
            termo = -termo
            print(' - ', end='')
        else:
            print(' + ', end='')
        print(f'{numero}/{int(numero ** 2)}', end="")
        resultado += termo

    print('\n',resultado)

calcular_serie()