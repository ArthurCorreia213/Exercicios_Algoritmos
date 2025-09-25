# Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde: 
# Casa:  1 2 3 4 ... 64 
# Qdte: 1 2 4 8 ... N 

#Arthur Correia
def calc_total():
    casas = 64
    total = 1
    for i in range(casas):
        print(total)
        total*=2

calc_total()