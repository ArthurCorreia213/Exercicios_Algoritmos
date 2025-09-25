# Receba 100 números inteiros reais. Verifique e mostre o maior e o menor 
# valor. Obs.: somente valores positivos. 

#Arthur Correia

def exibir_menor_e_maior(numeros):
    menor = min(numeros)
    while menor <0:
        numeros.remove(menor)
        if numeros == []:
            print("A lista só tem números negativos")
        else:
            menor = min(numeros)

    if numeros != []:
        maior = max(numeros)

    print(f"O menor núemro é {menor}\nO maior número é {maior}")

#100 inputs seriam entediantes e demorados, então preferi usar uma lista
#Usei list comprehension para criar a lista, basta trocar para testar com outros valores
lista = [i for i in range(1, 101)]

exibir_menor_e_maior(lista)