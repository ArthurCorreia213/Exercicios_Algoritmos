#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessáriamente em ordem. Mostre todos os números em ordem crescente
#Arthur Correia

def organizador_de_nums():
    valor_seq1 = int(input("Digite o primeiro valor (em ordem):"))
    valor_seq2 = int(input("Digite o segundo valor (em ordem):"))

    while valor_seq2<valor_seq1:
        valor_seq2 = int(input("Digite o segundo valor (em ordem):"))

    valor_seq3 = int(input("Digite o terceiro valor (em ordem): "))

    while valor_seq3<valor_seq2:
        valor_seq3 = int(input("Digite o terceiro valor (em ordem):"))


    valor_outro = int(input("Digite um valor qualquer: "))

    if valor_outro>valor_seq3:
        print(valor_seq1,valor_seq2,valor_seq3,valor_outro)

    elif valor_outro>valor_seq2:
        print(valor_seq1,valor_seq2,valor_outro,valor_seq3)

    elif valor_outro>valor_seq1:
        print(valor_seq1, valor_outro,valor_seq2,valor_seq3)
        
    else:
        print(valor_outro, valor_seq1, valor_seq2, valor_seq3)

organizador_de_nums()
