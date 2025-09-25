# Mostre todas as possibilidades de 2 dados de forma que a soma tenha como 
# resultado 7.
#Arthur Correia

def calcular_resultados_dado():
    lados = 6
    lista = []

    for resultado_dado_1 in range(lados+1):
        for resultado_dado_2 in range(lados+1):
            if resultado_dado_1 + resultado_dado_2 == 7:
                lista.append((resultado_dado_1, resultado_dado_2)) 

    print(lista)

calcular_resultados_dado()