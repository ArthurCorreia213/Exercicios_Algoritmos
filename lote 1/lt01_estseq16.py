horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: R$"))
desconto = float(input("Digite o percentual de desconto (apenas número): "))/100
numero_de_dependentes = int(input("Digite o número de dependentes: "))

salario = horas_trabalhadas*valor_por_hora

salario_liquido = (salario-(salario*desconto)) + (100*numero_de_dependentes)

print(f"O salário a receber é de R${salario_liquido}")