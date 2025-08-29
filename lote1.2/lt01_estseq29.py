tipo_investimento = int(input("Digite 1 para poupança, digite 2 para renda fixa: "))
investimento = float(input("Digite o valor de investimento: "))

if tipo_investimento == 1:
    print(f"Em 30 dias você terá {investimento*1.03:.2f}")
elif tipo_investimento == 2:
    print(f'Em 30 dias você terá {investimento*1.05:.2f}')