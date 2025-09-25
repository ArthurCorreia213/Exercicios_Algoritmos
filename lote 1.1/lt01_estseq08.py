#Receba o valor de um depósito em poupança. Calcule e mostre o valor 
#após 1 mês de aplicação sabendo que rende 1,3% a. m. 
#Arthur Correia

deposito = float(input("Digite um valor de depósito: R$"))
print(f"Após um mês em uma aplicação que rende 1,3% a.m você teria R${deposito*1.013:.2f}")