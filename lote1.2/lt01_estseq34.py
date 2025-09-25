#Receba um número. Calcule e mostre os resultados da tabuada desse número. 
#Arthur Correia

def tabuada():
    numero = int(input("Digite um número intero: "))

    for num in range(1,11):
        print(f"{numero} x {num} = {num*numero}")

tabuada()