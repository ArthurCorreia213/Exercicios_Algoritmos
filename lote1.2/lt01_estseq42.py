# Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99 
#Arthur Correia

def calcular_serie():
    resultado = 1
    print('1', end='')
    for numero in range(2,51):
        resultado+= numero/((numero*2)-1)
        print(f' + {numero}/{(numero*2)-1}', end='')

    print('\n', resultado)

calcular_serie()