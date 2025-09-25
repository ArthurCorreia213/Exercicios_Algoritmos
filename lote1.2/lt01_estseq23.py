#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessáriamente em ordem. Mostre todos os números em ordem crescente
#Arthur Correia
def organizador_de_nums(valor_seq1,valor_seq2,valor_seq3,valor_outro):

    if valor_outro>valor_seq3:
        print(valor_seq1,valor_seq2,valor_seq3,valor_outro)

    elif valor_outro>valor_seq2:
        print(valor_seq1,valor_seq2,valor_outro,valor_seq3)

    elif valor_outro>valor_seq1:
        print(valor_seq1, valor_outro,valor_seq2,valor_seq3)
        
    else:
        print(valor_outro, valor_seq1, valor_seq2, valor_seq3)

        
valor_1 = int(input("Digite o primeiro valor (em ordem):"))
valor_2 = int(input("Digite o segundo valor (em ordem):"))

while valor_2<valor_1:
    valor_2 = int(input("Digite o segundo valor (em ordem):"))

valor_3 = int(input("Digite o terceiro valor (em ordem): "))

while valor_3<valor_2:
    valor_3 = int(input("Digite o terceiro valor (em ordem):"))


valor_4 = int(input("Digite um valor qualquer: "))

organizador_de_nums(valor_1, valor_2, valor_3, valor_4)
