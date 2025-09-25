# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do 
# investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a 
# poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados. 

#Arthur Correia

def calcular_investimento():
    tipo_investimento = int(input("Digite 1 para poupança, digite 2 para renda fixa: "))

    while tipo_investimento not in [1,2]:
        tipo_investimento = int(input("Digite 1 para poupança, digite 2 para renda fixa: "))

    investimento = float(input("Digite o valor de investimento: "))

    if tipo_investimento == 1:
        print(f"Em 30 dias você terá {investimento*1.03:.2f}")
    elif tipo_investimento == 2:
        print(f'Em 30 dias você terá {investimento*1.05:.2f}')
    
calcular_investimento()